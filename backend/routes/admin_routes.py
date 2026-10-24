from flask import Blueprint, jsonify
from database.connection import create_tables, reset_database

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/create-tables', methods=['POST'])
def create_db_tables():
    """Crear todas las tablas"""
    try:
        create_tables()
        return jsonify({'message': 'Tablas creadas exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@admin_bp.route('/reset-database', methods=['POST'])
def reset_db():
    """Resetear la base de datos (¡CUIDADO!)"""
    try:
        reset_database()
        return jsonify({'message': 'Base de datos reseteada'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500