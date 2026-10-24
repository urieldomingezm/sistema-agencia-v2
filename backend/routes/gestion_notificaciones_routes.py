from flask import Blueprint, request, jsonify
from database.models import GestionNotificaciones
from services.gestion_notificaciones_service import GestionNotificacionesService

gestion_notificaciones_bp = Blueprint('gestion_notificaciones', __name__)
gestion_notificaciones_service = GestionNotificacionesService()

@gestion_notificaciones_bp.route('/', methods=['GET'])
def get_notificaciones():
    """Obtener todas las notificaciones"""
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        usuario_id = request.args.get('usuario_id', type=int)
        id_encargado = request.args.get('id_encargado')
        
        if usuario_id:
            notificaciones = gestion_notificaciones_service.get_notificaciones_by_usuario(usuario_id)
            return jsonify([notif.to_dict() for notif in notificaciones])
        
        if id_encargado:
            notificaciones = gestion_notificaciones_service.get_notificaciones_by_encargado(id_encargado)
            return jsonify([notif.to_dict() for notif in notificaciones])
        
        notificaciones = gestion_notificaciones_service.get_all_notificaciones(page, per_page)
        
        return jsonify({
            'notificaciones': [notif.to_dict() for notif in notificaciones.items],
            'total': notificaciones.total,
            'pages': notificaciones.pages,
            'current_page': page
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@gestion_notificaciones_bp.route('/<int:notificacion_id>', methods=['GET'])
def get_notificacion(notificacion_id):
    """Obtener una notificación por ID"""
    try:
        notificacion = gestion_notificaciones_service.get_notificacion_by_id(notificacion_id)
        if not notificacion:
            return jsonify({'error': 'Notificación no encontrada'}), 404
        return jsonify(notificacion.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@gestion_notificaciones_bp.route('/', methods=['POST'])
def create_notificacion():
    """Crear una nueva notificación"""
    try:
        data = request.get_json()
        
        if not data.get('notificacion_mensaje'):
            return jsonify({'error': 'notificacion_mensaje es requerido'}), 400
        
        notificacion = gestion_notificaciones_service.create_notificacion(data)
        return jsonify(notificacion.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@gestion_notificaciones_bp.route('/<int:notificacion_id>', methods=['PUT'])
def update_notificacion(notificacion_id):
    """Actualizar una notificación"""
    try:
        notificacion = gestion_notificaciones_service.get_notificacion_by_id(notificacion_id)
        if not notificacion:
            return jsonify({'error': 'Notificación no encontrada'}), 404
        
        data = request.get_json()
        notificacion = gestion_notificaciones_service.update_notificacion(notificacion, data)
        return jsonify(notificacion.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@gestion_notificaciones_bp.route('/<int:notificacion_id>', methods=['DELETE'])
def delete_notificacion(notificacion_id):
    """Eliminar una notificación"""
    try:
        notificacion = gestion_notificaciones_service.get_notificacion_by_id(notificacion_id)
        if not notificacion:
            return jsonify({'error': 'Notificación no encontrada'}), 404
        
        gestion_notificaciones_service.delete_notificacion(notificacion)
        return jsonify({'message': 'Notificación eliminada correctamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500