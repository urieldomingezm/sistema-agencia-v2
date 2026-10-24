from flask import Blueprint, request, jsonify
from database.models import GestionRequisitos
from services.gestion_requisitos_service import GestionRequisitosService

gestion_requisitos_bp = Blueprint('gestion_requisitos', __name__)
gestion_requisitos_service = GestionRequisitosService()

@gestion_requisitos_bp.route('/', methods=['GET'])
def get_requisitos():
    """Obtener todos los requisitos"""
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        user = request.args.get('user')
        is_completed = request.args.get('is_completed')
        
        if user:
            requisitos = gestion_requisitos_service.get_requisitos_by_user(user)
            return jsonify([requisito.to_dict() for requisito in requisitos])
        
        if is_completed:
            requisitos = gestion_requisitos_service.get_requisitos_completed(is_completed)
            return jsonify([requisito.to_dict() for requisito in requisitos])
        
        requisitos = gestion_requisitos_service.get_all_requisitos(page, per_page)
        
        return jsonify({
            'requisitos': [requisito.to_dict() for requisito in requisitos.items],
            'total': requisitos.total,
            'pages': requisitos.pages,
            'current_page': page
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@gestion_requisitos_bp.route('/<int:requisito_id>', methods=['GET'])
def get_requisito(requisito_id):
    """Obtener un requisito por ID"""
    try:
        requisito = gestion_requisitos_service.get_requisito_by_id(requisito_id)
        if not requisito:
            return jsonify({'error': 'Requisito no encontrado'}), 404
        return jsonify(requisito.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@gestion_requisitos_bp.route('/', methods=['POST'])
def create_requisito():
    """Crear un nuevo requisito"""
    try:
        data = request.get_json()
        
        if not data.get('user'):
            return jsonify({'error': 'user es requerido'}), 400
        
        requisito = gestion_requisitos_service.create_requisito(data)
        return jsonify(requisito.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@gestion_requisitos_bp.route('/<int:requisito_id>', methods=['PUT'])
def update_requisito(requisito_id):
    """Actualizar un requisito"""
    try:
        requisito = gestion_requisitos_service.get_requisito_by_id(requisito_id)
        if not requisito:
            return jsonify({'error': 'Requisito no encontrado'}), 404
        
        data = request.get_json()
        requisito = gestion_requisitos_service.update_requisito(requisito, data)
        return jsonify(requisito.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@gestion_requisitos_bp.route('/<int:requisito_id>', methods=['DELETE'])
def delete_requisito(requisito_id):
    """Eliminar un requisito"""
    try:
        requisito = gestion_requisitos_service.get_requisito_by_id(requisito_id)
        if not requisito:
            return jsonify({'error': 'Requisito no encontrado'}), 404
        
        gestion_requisitos_service.delete_requisito(requisito)
        return jsonify({'message': 'Requisito eliminado correctamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500