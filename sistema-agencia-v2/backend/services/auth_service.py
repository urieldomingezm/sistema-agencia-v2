from database import db
from database.models import RegistroUsuarios
from services.user_service import UserService

class AuthService:
    def __init__(self):
        self.user_service = UserService()
    
    def register_user(self, data, ip_address):
        """Registrar un nuevo usuario"""
        return self.user_service.create_user(data, ip_address)
    
    def authenticate_user(self, username, password):
        """Autenticar usuario"""
        user = self.user_service.get_user_by_username(username)
        if user and user.check_password(password):
            return user
        return None