from flask import Flask
from .user_routes import user_bp
from .auth_routes import auth_bp
from .admin_routes import admin_bp
from .historial_tiempos_routes import historial_tiempos_bp
from .historial_ascensos_routes import historial_ascensos_bp
from .gestion_ventas_routes import gestion_ventas_bp
from .gestion_tiempo_routes import gestion_tiempo_bp
from .gestion_requisitos_routes import gestion_requisitos_bp
from .ascensos_routes import ascensos_bp
from .gestion_notificaciones_routes import gestion_notificaciones_bp
from .gestion_pagas_routes import gestion_pagas_bp

def register_routes(app: Flask):
    """Registrar todas las rutas de la aplicación"""
    
    # Rutas existentes
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    
    # Nuevas rutas para las tablas
    app.register_blueprint(historial_tiempos_bp, url_prefix='/api/historial-tiempos')
    app.register_blueprint(historial_ascensos_bp, url_prefix='/api/historial-ascensos')
    app.register_blueprint(gestion_ventas_bp, url_prefix='/api/gestion-ventas')
    app.register_blueprint(gestion_tiempo_bp, url_prefix='/api/gestion-tiempo')
    app.register_blueprint(gestion_requisitos_bp, url_prefix='/api/gestion-requisitos')
    app.register_blueprint(ascensos_bp, url_prefix='/api/ascensos')
    app.register_blueprint(gestion_notificaciones_bp, url_prefix='/api/gestion-notificaciones')
    app.register_blueprint(gestion_pagas_bp, url_prefix='/api/gestion-pagas')
from flask import Blueprint

def register_routes(app):
    from routes.user_routes import user_bp
    from routes.auth_routes import auth_bp
    from routes.admin_routes import admin_bp
    
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')