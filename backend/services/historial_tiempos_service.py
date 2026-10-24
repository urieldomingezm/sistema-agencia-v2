from database import db
from database.models import HistorialTiempos
from datetime import datetime

class HistorialTiemposService:
    
    def create_historial_tiempo(self, data):
        """Crear un nuevo registro de historial de tiempos"""
        historial = HistorialTiempos(
            codigo_time=data['codigo_time'],
            tiempo_acumulado=data['tiempo_acumulado'],
            tiempo_transcurrido=data['tiempo_transcurrido'],
            tiempo_encargado_usuario=data.get('tiempo_encargado_usuario'),
            tiempo_fecha_registro=data.get('tiempo_fecha_registro', datetime.utcnow())
        )
        
        db.session.add(historial)
        db.session.commit()
        return historial
    
    def get_all_historial_tiempos(self, page=1, per_page=10):
        """Obtener todos los registros de historial de tiempos con paginación"""
        return HistorialTiempos.query.paginate(
            page=page, per_page=per_page, error_out=False
        )
    
    def get_historial_tiempo_by_id(self, historial_id):
        """Obtener un registro por ID"""
        return HistorialTiempos.query.get(historial_id)
    
    def get_historial_by_codigo_time(self, codigo_time):
        """Obtener historial por código de tiempo"""
        return HistorialTiempos.query.filter_by(codigo_time=codigo_time).all()
    
    def update_historial_tiempo(self, historial, data):
        """Actualizar un registro existente"""
        if 'tiempo_acumulado' in data:
            historial.tiempo_acumulado = data['tiempo_acumulado']
        if 'tiempo_transcurrido' in data:
            historial.tiempo_transcurrido = data['tiempo_transcurrido']
        if 'tiempo_encargado_usuario' in data:
            historial.tiempo_encargado_usuario = data['tiempo_encargado_usuario']
        
        db.session.commit()
        return historial
    
    def delete_historial_tiempo(self, historial):
        """Eliminar un registro"""
        db.session.delete(historial)
        db.session.commit()
        return True