from flask import Blueprint, request, jsonify
from database.models import HistorialAscensos
from services.historial_ascensos_service import HistorialAscensosService

historial_ascensos_bp = Blueprint('historial_ascensos', __name__)
historial_ascensos_service = HistorialAscensosService()

@historial_ascensos_bp.route('/', methods=['GET'])
def get_historial_ascensos():
    """Obtener todos los registros de historial de ascensos"""
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        codigo_time = request.args.get('codigo_time')
        
        if codigo_time:
            registros = historial_ascensos_service.get_historial_by_codigo_time(codigo_time)
            return jsonify([registro.to_dict() for registro in registros])
        
        registros = historial_ascensos_service.get_all_historial_ascensos(page, per_page)
        
        return jsonify({
            'registros': [registro.to_dict() for registro in registros.items],
            'total': registros.total,
            'pages': registros.pages,
            'current_page': page
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@historial_ascensos_bp.route('/<int:historial_id>', methods=['GET'])
def get_historial_ascenso(historial_id):
    """Obtener un registro por ID"""
    try:
        registro = historial_ascensos_service.get_historial_ascenso_by_id(historial_id)
        if not registro:
            return jsonify({'error': 'Registro no encontrado'}), 404
        return jsonify(registro.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@historial_ascensos_bp.route('/', methods=['POST'])
def create_historial_ascenso():
    """Crear un nuevo registro de historial de ascensos"""
    try:
        data = request.get_json()
        registro = historial_ascensos_service.create_historial_ascenso(data)
        return jsonify(registro.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@historial_ascensos_bp.route('/<int:historial_id>', methods=['PUT'])
def update_historial_ascenso(historial_id):
    """Actualizar un registro"""
    try:
        registro = historial_ascensos_service.get_historial_ascenso_by_id(historial_id)
        if not registro:
            return jsonify({'error': 'Registro no encontrado'}), 404
        
        data = request.get_json()
        registro = historial_ascensos_service.update_historial_ascenso(registro, data)
        return jsonify(registro.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@historial_ascensos_bp.route('/<int:historial_id>', methods=['DELETE'])
def delete_historial_ascenso(historial_id):
    """Eliminar un registro"""
    try:
        registro = historial_ascensos_service.get_historial_ascenso_by_id(historial_id)
        if not registro:
            return jsonify({'error': 'Registro no encontrado'}), 404
        
        historial_ascensos_service.delete_historial_ascenso(registro)
        return jsonify({'message': 'Registro eliminado correctamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500