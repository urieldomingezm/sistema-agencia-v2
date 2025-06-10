from database import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class RegistroUsuarios(db.Model):
    __tablename__ = 'registro_usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_registro = db.Column(db.String(50), nullable=False, unique=True)
    password_registro = db.Column(db.String(255), nullable=False)
    rol_id = db.Column(db.Integer, nullable=False, default=1)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    ip_registro = db.Column(db.String(45))
    nombre_habbo = db.Column(db.String(50))
    codigo_time = db.Column(db.String(20))
    ip_bloqueo = db.Column(db.String(45))
    activo = db.Column(db.Boolean, default=True)
    
    def set_password(self, password):
        self.password_registro = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_registro, password)
    
    def to_dict(self):
        return {
            'id': self.id,
            'usuario_registro': self.usuario_registro,
            'rol_id': self.rol_id,
            'fecha_registro': self.fecha_registro.isoformat() if self.fecha_registro else None,
            'ip_registro': self.ip_registro,
            'nombre_habbo': self.nombre_habbo,
            'codigo_time': self.codigo_time,
            'activo': self.activo
        }
    
    def __repr__(self):
        return f'<Usuario {self.usuario_registro}>'

class Roles(db.Model):
    __tablename__ = 'roles'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre_rol = db.Column(db.String(50), nullable=False, unique=True)
    descripcion = db.Column(db.Text)
    activo = db.Column(db.Boolean, default=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre_rol': self.nombre_rol,
            'descripcion': self.descripcion,
            'activo': self.activo
        }