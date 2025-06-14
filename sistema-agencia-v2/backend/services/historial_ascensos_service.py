from database import db
from database.models import HistorialAscensos
from datetime import datetime

class HistorialAscensosService:
    
    def create_historial_ascenso(self, data):
        """Crear un nuevo registro de historial de ascensos"""
        historial = HistorialAscensos(
            codigo_time=data.get('codigo_time'),
            rango_actual=data.get('rango_actual'),
            mision_actual=data.get('mision_actual'),
            firma_usuario=data.get('firma_usuario'),
            firma_encargado=data.get('firma_encargado'),
            estado_ascenso=data.get('estado_ascenso'),
            fecha_ultimo_ascenso=data.get('fecha_ultimo_ascenso'),
            fecha_disponible_ascenso=data.get('fecha_disponible_ascenso'),
            usuario_encargado=data.get('usuario_encargado'),
            accion=data.get('accion'),
            realizado_por=data.get('realizado_por')
        )
        
        db.session.add(historial)
        db.session.commit()
        return historial
    
    def get_all_historial_ascensos(self, page=1, per_page=10):
        """Obtener todos los registros con paginación"""
        return HistorialAscensos.query.paginate(
            page=page, per_page=per_page, error_out=False
        )
    
    def get_historial_ascenso_by_id(self, historial_id):
        """Obtener un registro por ID"""
        return HistorialAscensos.query.get(historial_id)
    
    def get_historial_by_codigo_time(self, codigo_time):
        """Obtener historial por código de tiempo"""
        return HistorialAscensos.query.filter_by(codigo_time=codigo_time).all()
    
    def update_historial_ascenso(self, historial, data):
        """Actualizar un registro existente"""
        for field in ['rango_actual', 'mision_actual', 'firma_usuario', 'firma_encargado', 
                     'estado_ascenso', 'usuario_encargado', 'accion', 'realizado_por']:
            if field in data:
                setattr(historial, field, data[field])
        
        db.session.commit()
        return historial
    
    def delete_historial_ascenso(self, historial):
        """Eliminar un registro"""
        db.session.delete(historial)
        db.session.commit()
        return True