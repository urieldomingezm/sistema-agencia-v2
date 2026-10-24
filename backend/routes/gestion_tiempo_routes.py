from flask import Blueprint, request, jsonify
from database.models import GestionTiempo
from services.gestion_tiempo_service import GestionTiempoService

gestion_tiempo_bp = Blueprint('gestion_tiempo', __name__)
gestion_tiempo_service = GestionTiempoService()

@gestion_tiempo_bp.route('/', methods=['GET'])
def get_gestion_tiempo():
    """Obtener todos los registros de gestión de tiempo"""
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        codigo_time = request.args.get('codigo_time')
        status = request.args.get('status')
        
        if codigo_time:
            gestion = gestion_tiempo_service.get_gestion_by_codigo_time(codigo_time)
            return jsonify(gestion.to_dict() if gestion else {})
        
        if status:
            gestiones = gestion_tiempo_service.get_gestion_by_status(status)
            return jsonify([gestion.to_dict() for gestion in gestiones])
        
        gestiones = gestion_tiempo_service.get_all_gestion_tiempo(page, per_page)
        
        return jsonify({
            'gestiones': [gestion.to_dict() for gestion in gestiones.items],
            'total': gestiones.total,
            'pages': gestiones.pages,
            'current_page': page
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@gestion_tiempo_bp.route('/<int:tiempo_id>', methods=['GET'])
def get_tiempo(tiempo_id):
    """Obtener un registro por ID"""
    try:
        gestion = gestion_tiempo_service.get_gestion_tiempo_by_id(tiempo_id)
        if not gestion:
            return jsonify({'error': 'Registro no encontrado'}), 404
        return jsonify(gestion.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@gestion_tiempo_bp.route('/', methods=['POST'])
def create_gestion_tiempo():
    """Crear un nuevo registro de gestión de tiempo"""
    try:
        data = request.get_json()
        
        if not data.get('codigo_time'):
            return jsonify({'error': 'codigo_time es requerido'}), 400
        
        gestion = gestion_tiempo_service.create_gestion_tiempo(data)
        return jsonify(gestion.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@gestion_tiempo_bp.route('/<int:tiempo_id>', methods=['PUT'])
def update_gestion_tiempo(tiempo_id):
    """Actualizar un registro"""
    try:
        gestion = gestion_tiempo_service.get_gestion_tiempo_by_id(tiempo_id)
        if not gestion:
            return jsonify({'error': 'Registro no encontrado'}), 404
        
        data = request.get_json()
        gestion = gestion_tiempo_service.update_gestion_tiempo(gestion, data)
        return jsonify(gestion.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@gestion_tiempo_bp.route('/<int:tiempo_id>', methods=['DELETE'])
def delete_gestion_tiempo(tiempo_id):
    """Eliminar un registro"""
    try:
        gestion = gestion_tiempo_service.get_gestion_tiempo_by_id(tiempo_id)
        if not gestion:
            return jsonify({'error': 'Registro no encontrado'}), 404
        
        gestion_tiempo_service.delete_gestion_tiempo(gestion)
        return jsonify({'message': 'Registro eliminado correctamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500