from flask import Blueprint, request, jsonify
from database.models import Ascensos
from services.ascensos_service import AscensosService

ascensos_bp = Blueprint('ascensos', __name__)
ascensos_service = AscensosService()

@ascensos_bp.route('/', methods=['GET'])
def get_ascensos():
    """Obtener todos los ascensos"""
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        codigo_time = request.args.get('codigo_time')
        estado = request.args.get('estado')
        pendientes = request.args.get('pendientes')
        
        if codigo_time:
            ascensos = ascensos_service.get_ascensos_by_codigo_time(codigo_time)
            return jsonify([ascenso.to_dict() for ascenso in ascensos])
        
        if estado:
            ascensos = ascensos_service.get_ascensos_by_estado(estado)
            return jsonify([ascenso.to_dict() for ascenso in ascensos])
        
        if pendientes == 'true':
            ascensos = ascensos_service.get_ascensos_pendientes()
            return jsonify([ascenso.to_dict() for ascenso in ascensos])
        
        ascensos = ascensos_service.get_all_ascensos(page, per_page)
        
        return jsonify({
            'ascensos': [ascenso.to_dict() for ascenso in ascensos.items],
            'total': ascensos.total,
            'pages': ascensos.pages,
            'current_page': page
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@ascensos_bp.route('/<int:ascenso_id>', methods=['GET'])
def get_ascenso(ascenso_id):
    """Obtener un ascenso por ID"""
    try:
        ascenso = ascensos_service.get_ascenso_by_id(ascenso_id)
        if not ascenso:
            return jsonify({'error': 'Ascenso no encontrado'}), 404
        return jsonify(ascenso.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@ascensos_bp.route('/', methods=['POST'])
def create_ascenso():
    """Crear un nuevo ascenso"""
    try:
        data = request.get_json()
        
        required_fields = ['codigo_time', 'rango_actual']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'{field} es requerido'}), 400
        
        ascenso = ascensos_service.create_ascenso(data)
        return jsonify(ascenso.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@ascensos_bp.route('/<int:ascenso_id>', methods=['PUT'])
def update_ascenso(ascenso_id):
    """Actualizar un ascenso"""
    try:
        ascenso = ascensos_service.get_ascenso_by_id(ascenso_id)
        if not ascenso:
            return jsonify({'error': 'Ascenso no encontrado'}), 404
        
        data = request.get_json()
        ascenso = ascensos_service.update_ascenso(ascenso, data)
        return jsonify(ascenso.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@ascensos_bp.route('/<int:ascenso_id>', methods=['DELETE'])
def delete_ascenso(ascenso_id):
    """Eliminar un ascenso"""
    try:
        ascenso = ascensos_service.get_ascenso_by_id(ascenso_id)
        if not ascenso:
            return jsonify({'error': 'Ascenso no encontrado'}), 404
        
        ascensos_service.delete_ascenso(ascenso)
        return jsonify({'message': 'Ascenso eliminado correctamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500