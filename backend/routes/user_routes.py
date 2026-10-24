from flask import Blueprint, request, jsonify
from database import db
from database.models import RegistroUsuarios
from services.user_service import UserService

user_bp = Blueprint('users', __name__)
user_service = UserService()

@user_bp.route('/', methods=['GET'])
def get_users():
    """Obtener todos los usuarios"""
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        
        users = RegistroUsuarios.query.paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return jsonify({
            'users': [user.to_dict() for user in users.items],
            'total': users.total,
            'pages': users.pages,
            'current_page': page
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Obtener un usuario por ID"""
    try:
        user = RegistroUsuarios.query.get_or_404(user_id)
        return jsonify(user.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@user_bp.route('/', methods=['POST'])
def create_user():
    """Crear un nuevo usuario"""
    try:
        data = request.get_json()
        
        # Validar datos requeridos
        if not data.get('usuario_registro') or not data.get('password_registro'):
            return jsonify({'error': 'Usuario y contraseña son requeridos'}), 400
        
        # Verificar si el usuario ya existe
        if RegistroUsuarios.query.filter_by(usuario_registro=data['usuario_registro']).first():
            return jsonify({'error': 'El usuario ya existe'}), 409
        
        user = user_service.create_user(data, request.remote_addr)
        return jsonify(user.to_dict()), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Actualizar un usuario"""
    try:
        user = RegistroUsuarios.query.get_or_404(user_id)
        data = request.get_json()
        
        user = user_service.update_user(user, data)
        return jsonify(user.to_dict())
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Eliminar un usuario (hard delete)"""
    try:
        user = RegistroUsuarios.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        
        return jsonify({'message': 'Usuario eliminado correctamente'})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500