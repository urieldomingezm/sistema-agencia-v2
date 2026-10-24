from database import db
from database.models import Ascensos
from datetime import datetime

class AscensosService:
    
    def create_ascenso(self, data):
        """Crear un nuevo ascenso"""
        ascenso = Ascensos(
            codigo_time=data['codigo_time'],
            rango_actual=data['rango_actual'],
            mision_actual=data.get('mision_actual'),
            firma_usuario=data.get('firma_usuario'),
            firma_encargado=data.get('firma_encargado'),
            estado_ascenso=data.get('estado_ascenso', 'pendiente'),
            fecha_disponible_ascenso=data.get('fecha_disponible_ascenso'),
            usuario_encargado=data.get('usuario_encargado'),
            es_recluta=data.get('es_recluta', False)
        )
        
        db.session.add(ascenso)
        db.session.commit()
        return ascenso
    
    def get_all_ascensos(self, page=1, per_page=10):
        """Obtener todos los ascensos con paginación"""
        return Ascensos.query.paginate(
            page=page, per_page=per_page, error_out=False
        )
    
    def get_ascenso_by_id(self, ascenso_id):
        """Obtener un ascenso por ID"""
        return Ascensos.query.get(ascenso_id)
    
    def get_ascensos_by_codigo_time(self, codigo_time):
        """Obtener ascensos por código de tiempo"""
        return Ascensos.query.filter_by(codigo_time=codigo_time).all()
    
    def get_ascensos_by_estado(self, estado):
        """Obtener ascensos por estado"""
        return Ascensos.query.filter_by(estado_ascenso=estado).all()
    
    def get_ascensos_pendientes(self):
        """Obtener ascensos pendientes"""
        return Ascensos.query.filter_by(estado_ascenso='pendiente').all()
    
    def update_ascenso(self, ascenso, data):
        """Actualizar un ascenso existente"""
        for field in ['rango_actual', 'mision_actual', 'firma_usuario', 'firma_encargado', 
                     'estado_ascenso', 'fecha_disponible_ascenso', 'usuario_encargado', 'es_recluta']:
            if field in data:
                setattr(ascenso, field, data[field])
        
        db.session.commit()
        return ascenso
    
    def delete_ascenso(self, ascenso):
        """Eliminar un ascenso"""
        db.session.delete(ascenso)
        db.session.commit()
        return True