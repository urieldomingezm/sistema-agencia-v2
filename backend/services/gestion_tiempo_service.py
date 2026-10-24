from database import db
from database.models import GestionTiempo
from datetime import datetime, time

class GestionTiempoService:
    
    def create_gestion_tiempo(self, data):
        """Crear un nuevo registro de gestión de tiempo"""
        gestion = GestionTiempo(
            codigo_time=data['codigo_time'],
            tiempo_status=data.get('tiempo_status', 'disponible'),
            tiempo_restado=data.get('tiempo_restado', time(0, 0, 0)),
            tiempo_acumulado=data.get('tiempo_acumulado', time(0, 0, 0)),
            tiempo_transcurrido=data.get('tiempo_transcurrido', time(0, 0, 0)),
            tiempo_encargado_usuario=data.get('tiempo_encargado_usuario'),
            tiempo_iniciado=data.get('tiempo_iniciado')
        )
        
        db.session.add(gestion)
        db.session.commit()
        return gestion
    
    def get_all_gestion_tiempo(self, page=1, per_page=10):
        """Obtener todos los registros con paginación"""
        return GestionTiempo.query.paginate(
            page=page, per_page=per_page, error_out=False
        )
    
    def get_gestion_tiempo_by_id(self, tiempo_id):
        """Obtener un registro por ID"""
        return GestionTiempo.query.get(tiempo_id)
    
    def get_gestion_by_codigo_time(self, codigo_time):
        """Obtener gestión por código de tiempo"""
        return GestionTiempo.query.filter_by(codigo_time=codigo_time).first()
    
    def get_gestion_by_status(self, status):
        """Obtener gestiones por estado"""
        return GestionTiempo.query.filter_by(tiempo_status=status).all()
    
    def update_gestion_tiempo(self, gestion, data):
        """Actualizar un registro existente"""
        for field in ['tiempo_status', 'tiempo_restado', 'tiempo_acumulado', 
                     'tiempo_transcurrido', 'tiempo_encargado_usuario', 'tiempo_iniciado']:
            if field in data:
                setattr(gestion, field, data[field])
        
        db.session.commit()
        return gestion
    
    def delete_gestion_tiempo(self, gestion):
        """Eliminar un registro"""
        db.session.delete(gestion)
        db.session.commit()
        return True