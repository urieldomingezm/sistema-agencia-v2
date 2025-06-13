from database import db
from database.models import GestionPagas
from datetime import datetime

class GestionPagasService:
    
    def create_paga(self, data):
        """Crear una nueva paga"""
        paga = GestionPagas(
            pagas_usuario=data['pagas_usuario'],
            pagas_rango=data['pagas_rango'],
            pagas_recibio=data['pagas_recibio'],
            pagas_motivo=data.get('pagas_motivo'),
            pagas_completo=data['pagas_completo'],
            pagas_descripcion=data.get('pagas_descripcion')
        )
        
        db.session.add(paga)
        db.session.commit()
        return paga
    
    def get_all_pagas(self, page=1, per_page=10):
        """Obtener todas las pagas con paginación"""
        return GestionPagas.query.paginate(
            page=page, per_page=per_page, error_out=False
        )
    
    def get_paga_by_id(self, paga_id):
        """Obtener una paga por ID"""
        return GestionPagas.query.get(paga_id)
    
    def get_pagas_by_usuario(self, usuario):
        """Obtener pagas por usuario"""
        return GestionPagas.query.filter_by(pagas_usuario=usuario).all()
    
    def get_pagas_by_rango(self, rango):
        """Obtener pagas por rango"""
        return GestionPagas.query.filter_by(pagas_rango=rango).all()
    
    def update_paga(self, paga, data):
        """Actualizar una paga existente"""
        for field in ['pagas_usuario', 'pagas_rango', 'pagas_recibio', 
                     'pagas_motivo', 'pagas_completo', 'pagas_descripcion']:
            if field in data:
                setattr(paga, field, data[field])
        
        db.session.commit()
        return paga
    
    def delete_paga(self, paga):
        """Eliminar una paga"""
        db.session.delete(paga)
        db.session.commit()
        return True