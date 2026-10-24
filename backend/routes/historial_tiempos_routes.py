from flask import Blueprint, request, jsonify
from database.models import HistorialTiempos
from services.historial_tiempos_service import HistorialTiemposService

historial_tiempos_bp = Blueprint('historial_tiempos', __name__)
historial_tiempos_service = HistorialTiemposService()

@historial_tiempos_bp.route('/', methods=['GET'])
def get_historial_tiempos():
    """Obtener todos los registros de historial de tiempos"""
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        codigo_time = request.args.get('codigo_time')
        
        if codigo_time:
            registros = historial_tiempos_service.get_historial_by_codigo_time(codigo_time)
            return jsonify([registro.to_dict() for registro in registros])
        
        registros = historial_tiempos_service.get_all_historial_tiempos(page, per_page)
        
        return jsonify({
            'registros': [registro.to_dict() for registro in registros.items],
            'total': registros.total,
            'pages': registros.pages,
            'current_page': page
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@historial_tiempos_bp.route('/<int:historial_id>', methods=['GET'])
def get_historial_tiempo(historial_id):
    """Obtener un registro por ID"""
    try:
        registro = historial_tiempos_service.get_historial_tiempo_by_id(historial_id)
        if not registro:
            return jsonify({'error': 'Registro no encontrado'}), 404
        return jsonify(registro.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@historial_tiempos_bp.route('/', methods=['POST'])
def create_historial_tiempo():
    """Crear un nuevo registro de historial de tiempos"""
    try:
        data = request.get_json()
        
        # Validar datos requeridos
        required_fields = ['codigo_time', 'tiempo_acumulado', 'tiempo_transcurrido']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'{field} es requerido'}), 400
        
        registro = historial_tiempos_service.create_historial_tiempo(data)
        return jsonify(registro.to_dict()), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@historial_tiempos_bp.route('/<int:historial_id>', methods=['PUT'])
def update_historial_tiempo(historial_id):
    """Actualizar un registro"""
    try:
        registro = historial_tiempos_service.get_historial_tiempo_by_id(historial_id)
        if not registro:
            return jsonify({'error': 'Registro no encontrado'}), 404
        
        data = request.get_json()
        registro = historial_tiempos_service.update_historial_tiempo(registro, data)
        return jsonify(registro.to_dict())
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@historial_tiempos_bp.route('/<int:historial_id>', methods=['DELETE'])
def delete_historial_tiempo(historial_id):
    """Eliminar un registro"""
    try:
        registro = historial_tiempos_service.get_historial_tiempo_by_id(historial_id)
        if not registro:
            return jsonify({'error': 'Registro no encontrado'}), 404
        
        historial_tiempos_service.delete_historial_tiempo(registro)
        return jsonify({'message': 'Registro eliminado correctamente'})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500