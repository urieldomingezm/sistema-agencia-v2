from database import db
from database.models import GestionNotificaciones
from datetime import datetime

class GestionNotificacionesService:
    
    def create_notificacion(self, data):
        """Crear una nueva notificación"""
        notificacion = GestionNotificaciones(
            notificacion_mensaje=data['notificacion_mensaje'],
            usuario_id=data.get('usuario_id'),
            id_encargado=data.get('id_encargado')
        )
        
        db.session.add(notificacion)
        db.session.commit()
        return notificacion
    
    def get_all_notificaciones(self, page=1, per_page=10):
        """Obtener todas las notificaciones con paginación"""
        return GestionNotificaciones.query.paginate(
            page=page, per_page=per_page, error_out=False
        )
    
    def get_notificacion_by_id(self, notificacion_id):
        """Obtener una notificación por ID"""
        return GestionNotificaciones.query.get(notificacion_id)
    
    def get_notificaciones_by_usuario(self, usuario_id):
        """Obtener notificaciones por usuario"""
        return GestionNotificaciones.query.filter_by(usuario_id=usuario_id).all()
    
    def get_notificaciones_by_encargado(self, id_encargado):
        """Obtener notificaciones por encargado"""
        return GestionNotificaciones.query.filter_by(id_encargado=id_encargado).all()
    
    def update_notificacion(self, notificacion, data):
        """Actualizar una notificación existente"""
        for field in ['notificacion_mensaje', 'usuario_id', 'id_encargado']:
            if field in data:
                setattr(notificacion, field, data[field])
        
        db.session.commit()
        return notificacion
    
    def delete_notificacion(self, notificacion):
        """Eliminar una notificación"""
        db.session.delete(notificacion)
        db.session.commit()
        return True