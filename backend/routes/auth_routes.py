from flask import Blueprint, request, jsonify
from database.models import RegistroUsuarios
from services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)
auth_service = AuthService()

@auth_bp.route('/login', methods=['POST'])
def login():
    """Iniciar sesión"""
    try:
        data = request.get_json()
        usuario = data.get('usuario_registro')
        password = data.get('password_registro')
        
        if not usuario or not password:
            return jsonify({'error': 'Usuario y contraseña requeridos'}), 400
        
        user = RegistroUsuarios.query.filter_by(usuario_registro=usuario).first()
        
        if user and user.check_password(password):
            # Aquí puedes agregar JWT tokens más adelante
            return jsonify({
                'message': 'Login exitoso',
                'user': user.to_dict()
            })
        else:
            return jsonify({'error': 'Credenciales inválidas'}), 401
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auth_bp.route('/register', methods=['POST'])
def register():
    """Registrar nuevo usuario"""
    try:
        data = request.get_json()
        
        if not data.get('usuario_registro') or not data.get('password_registro'):
            return jsonify({'error': 'Usuario y contraseña requeridos'}), 400
        
        if RegistroUsuarios.query.filter_by(usuario_registro=data['usuario_registro']).first():
            return jsonify({'error': 'El usuario ya existe'}), 409
        
        user = auth_service.register_user(data, request.remote_addr)
        return jsonify({
            'message': 'Usuario registrado exitosamente',
            'user': user.to_dict()
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500