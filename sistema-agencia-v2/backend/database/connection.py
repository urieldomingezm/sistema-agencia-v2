from database import db

def create_tables():
    """Crear todas las tablas"""
    db.create_all()

def drop_tables():
    """Eliminar todas las tablas"""
    db.drop_all()

def reset_database():
    """Resetear la base de datos"""
    drop_tables()
    create_tables()