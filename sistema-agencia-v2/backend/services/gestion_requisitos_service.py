from database import db
from database.models import GestionRequisitos
from datetime import datetime

class GestionRequisitosService:
    
    def create_requisito(self, data):
        """Crear un nuevo requisito"""
        requisito = GestionRequisitos(
            user=data['user'],
            requirement_name=data.get('requirement_name'),
            times_as_encargado_count=data.get('times_as_encargado_count', 0),
            ascensos_as_encargado_count=data.get('ascensos_as_encargado_count', 0),
            is_completed=data.get('is_completed')
        )
        
        db.session.add(requisito)
        db.session.commit()
        return requisito
    
    def get_all_requisitos(self, page=1, per_page=10):
        """Obtener todos los requisitos con paginación"""
        return GestionRequisitos.query.paginate(
            page=page, per_page=per_page, error_out=False
        )
    
    def get_requisito_by_id(self, requisito_id):
        """Obtener un requisito por ID"""
        return GestionRequisitos.query.get(requisito_id)
    
    def get_requisitos_by_user(self, user):
        """Obtener requisitos por usuario"""
        return GestionRequisitos.query.filter_by(user=user).all()
    
    def get_requisitos_completed(self, is_completed):
        """Obtener requisitos por estado de completado"""
        return GestionRequisitos.query.filter_by(is_completed=is_completed).all()
    
    def update_requisito(self, requisito, data):
        """Actualizar un requisito existente"""
        for field in ['requirement_name', 'times_as_encargado_count', 
                     'ascensos_as_encargado_count', 'is_completed']:
            if field in data:
                setattr(requisito, field, data[field])
        
        db.session.commit()
        return requisito
    
    def delete_requisito(self, requisito):
        """Eliminar un requisito"""
        db.session.delete(requisito)
        db.session.commit()
        return True