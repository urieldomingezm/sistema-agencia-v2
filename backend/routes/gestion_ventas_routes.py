from flask import Blueprint, request, jsonify
from database.models import GestionVentas
from services.gestion_ventas_service import GestionVentasService

gestion_ventas_bp = Blueprint('gestion_ventas', __name__)
gestion_ventas_service = GestionVentasService()

@gestion_ventas_bp.route('/', methods=['GET'])
def get_ventas():
    """Obtener todas las ventas"""
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        estado = request.args.get('estado')
        encargado = request.args.get('encargado')
        
        if estado:
            ventas = gestion_ventas_service.get_ventas_by_estado(estado)
            return jsonify([venta.to_dict() for venta in ventas])
        
        if encargado:
            ventas = gestion_ventas_service.get_ventas_by_encargado(encargado)
            return jsonify([venta.to_dict() for venta in ventas])
        
        ventas = gestion_ventas_service.get_all_ventas(page, per_page)
        
        return jsonify({
            'ventas': [venta.to_dict() for venta in ventas.items],
            'total': ventas.total,
            'pages': ventas.pages,
            'current_page': page
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@gestion_ventas_bp.route('/<int:venta_id>', methods=['GET'])
def get_venta(venta_id):
    """Obtener una venta por ID"""
    try:
        venta = gestion_ventas_service.get_venta_by_id(venta_id)
        if not venta:
            return jsonify({'error': 'Venta no encontrada'}), 404
        return jsonify(venta.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@gestion_ventas_bp.route('/', methods=['POST'])
def create_venta():
    """Crear una nueva venta"""
    try:
        data = request.get_json()
        
        required_fields = ['venta_titulo', 'venta_compra', 'venta_caducidad', 'venta_estado', 'venta_costo']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'{field} es requerido'}), 400
        
        venta = gestion_ventas_service.create_venta(data)
        return jsonify(venta.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@gestion_ventas_bp.route('/<int:venta_id>', methods=['PUT'])
def update_venta(venta_id):
    """Actualizar una venta"""
    try:
        venta = gestion_ventas_service.get_venta_by_id(venta_id)
        if not venta:
            return jsonify({'error': 'Venta no encontrada'}), 404
        
        data = request.get_json()
        venta = gestion_ventas_service.update_venta(venta, data)
        return jsonify(venta.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@gestion_ventas_bp.route('/<int:venta_id>', methods=['DELETE'])
def delete_venta(venta_id):
    """Eliminar una venta"""
    try:
        venta = gestion_ventas_service.get_venta_by_id(venta_id)
        if not venta:
            return jsonify({'error': 'Venta no encontrada'}), 404
        
        gestion_ventas_service.delete_venta(venta)
        return jsonify({'message': 'Venta eliminada correctamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500