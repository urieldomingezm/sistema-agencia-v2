from flask import Flask, jsonify
from flask_cors import CORS
from config import config
from database import init_db
from routes import register_routes
from database.connection import create_tables
import os

def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'default')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    CORS(app)
    db = init_db(app)
    
    register_routes(app)
    
    @app.route('/health')
    def health_check():
        return jsonify({'status': 'OK', 'message': 'API funcionando correctamente'})
    
    @app.route('/')
    def hello():
        return jsonify({
            'message': 'API RESTful de Sistema Agencia',
            'version': '1.0.0',
            'endpoints': {
                'users': '/api/users',
                'auth': '/api/auth',
                'admin': '/api/admin',
                'health': '/health'
            }
        })
    
    # Crear tablas al iniciar
    with app.app_context():
        create_tables()
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)