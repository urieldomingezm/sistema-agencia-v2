from database import db
from database.models import GestionVentas
from datetime import datetime

class GestionVentasService:
    
    def create_venta(self, data):
        """Crear una nueva venta"""
        venta = GestionVentas(
            venta_titulo=data['venta_titulo'],
            venta_compra=data['venta_compra'],
            venta_caducidad=data['venta_caducidad'],
            venta_estado=data['venta_estado'],
            venta_costo=data['venta_costo'],
            venta_comprador=data.get('venta_comprador'),
            comprador_externo=data.get('comprador_externo'),
            venta_encargado=data.get('venta_encargado'),
            venta_fecha_compra=data.get('venta_fecha_compra')
        )
        
        db.session.add(venta)
        db.session.commit()
        return venta
    
    def get_all_ventas(self, page=1, per_page=10):
        """Obtener todas las ventas con paginación"""
        return GestionVentas.query.paginate(
            page=page, per_page=per_page, error_out=False
        )
    
    def get_venta_by_id(self, venta_id):
        """Obtener una venta por ID"""
        return GestionVentas.query.get(venta_id)
    
    def get_ventas_by_estado(self, estado):
        """Obtener ventas por estado"""
        return GestionVentas.query.filter_by(venta_estado=estado).all()
    
    def get_ventas_by_encargado(self, encargado):
        """Obtener ventas por encargado"""
        return GestionVentas.query.filter_by(venta_encargado=encargado).all()
    
    def update_venta(self, venta, data):
        """Actualizar una venta existente"""
        for field in ['venta_titulo', 'venta_compra', 'venta_caducidad', 'venta_estado', 
                     'venta_costo', 'venta_comprador', 'comprador_externo', 'venta_encargado', 'venta_fecha_compra']:
            if field in data:
                setattr(venta, field, data[field])
        
        db.session.commit()
        return venta
    
    def delete_venta(self, venta):
        """Eliminar una venta"""
        db.session.delete(venta)
        db.session.commit()
        return True