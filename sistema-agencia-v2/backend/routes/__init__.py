from flask import Blueprint

def register_routes(app):
    from routes.user_routes import user_bp
    from routes.auth_routes import auth_bp
    from routes.admin_routes import admin_bp
    
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')