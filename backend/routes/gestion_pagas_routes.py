from flask import Blueprint, request, jsonify
from database.models import GestionPagas
from services.gestion_pagas_service import GestionPagasService

gestion_pagas_bp = Blueprint('gestion_pagas', __name__)
gestion_pagas_service = GestionPagasService()

@gestion_pagas_bp.route('/', methods=['GET'])
def get_pagas():
    """Obtener todas las pagas"""
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        usuario = request.args.get('usuario')
        rango = request.args.get('rango')
        
        if usuario:
            pagas = gestion_pagas_service.get_pagas_by_usuario(usuario)
            return jsonify([paga.to_dict() for paga in pagas])
        
        if rango:
            pagas = gestion_pagas_service.get_pagas_by_rango(rango)
            return jsonify([paga.to_dict() for paga in pagas])
        
        pagas = gestion_pagas_service.get_all_pagas(page, per_page)
        
        return jsonify({
            'pagas': [paga.to_dict() for paga in pagas.items],
            'total': pagas.total,
            'pages': pagas.pages,
            'current_page': page
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@gestion_pagas_bp.route('/<int:paga_id>', methods=['GET'])
def get_paga(paga_id):
    """Obtener una paga por ID"""
    try:
        paga = gestion_pagas_service.get_paga_by_id(paga_id)
        if not paga:
            return jsonify({'error': 'Paga no encontrada'}), 404
        return jsonify(paga.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@gestion_pagas_bp.route('/', methods=['POST'])
def create_paga():
    """Crear una nueva paga"""
    try:
        data = request.get_json()
        
        required_fields = ['pagas_usuario', 'pagas_rango', 'pagas_recibio', 'pagas_completo']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'{field} es requerido'}), 400
        
        paga = gestion_pagas_service.create_paga(data)
        return jsonify(paga.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@gestion_pagas_bp.route('/<int:paga_id>', methods=['PUT'])
def update_paga(paga_id):
    """Actualizar una paga"""
    try:
        paga = gestion_pagas_service.get_paga_by_id(paga_id)
        if not paga:
            return jsonify({'error': 'Paga no encontrada'}), 404
        
        data = request.get_json()
        paga = gestion_pagas_service.update_paga(paga, data)
        return jsonify(paga.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@gestion_pagas_bp.route('/<int:paga_id>', methods=['DELETE'])
def delete_paga(paga_id):
    """Eliminar una paga"""
    try:
        paga = gestion_pagas_service.get_paga_by_id(paga_id)
        if not paga:
            return jsonify({'error': 'Paga no encontrada'}), 404
        
        gestion_pagas_service.delete_paga(paga)
        return jsonify({'message': 'Paga eliminada correctamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500