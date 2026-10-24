from database import db
from database.models import RegistroUsuarios
from datetime import datetime

class UserService:
    
    def create_user(self, data, ip_address):
        """Crear un nuevo usuario"""
        user = RegistroUsuarios(
            usuario_registro=data['usuario_registro'],
            ip_registro=ip_address,
            nombre_habbo=data.get('nombre_habbo'),
            codigo_time=data.get('codigo_time')
        )
        user.set_password(data['password_registro'])
        
        db.session.add(user)
        db.session.commit()
        return user
    
    def update_user(self, user, data):
        """Actualizar un usuario existente"""
        if 'nombre_habbo' in data:
            user.nombre_habbo = data['nombre_habbo']
        if 'codigo_time' in data:
            user.codigo_time = data['codigo_time']
        
        db.session.commit()
        return user
    
    def get_user_by_username(self, username):
        """Obtener usuario por nombre de usuario"""
        return RegistroUsuarios.query.filter_by(usuario_registro=username).first()