from database import db
from datetime import datetime, time
from werkzeug.security import generate_password_hash, check_password_hash

class RegistroUsuarios(db.Model):
    __tablename__ = 'registro_usuario'
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_registro = db.Column(db.String(50), nullable=False, unique=True)
    password_registro = db.Column(db.String(255), nullable=False)
    fecha_registro = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    ip_registro = db.Column(db.String(30), nullable=False)
    nombre_habbo = db.Column(db.String(50), unique=True)
    codigo_time = db.Column(db.String(5), unique=True)
    ip_bloqueo = db.Column(db.String(255))
    
    def set_password(self, password):
        self.password_registro = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_registro, password)
    
    def to_dict(self):
        return {
            'id': self.id,
            'usuario_registro': self.usuario_registro,
            'fecha_registro': self.fecha_registro.isoformat() if self.fecha_registro else None,
            'ip_registro': self.ip_registro,
            'nombre_habbo': self.nombre_habbo,
            'codigo_time': self.codigo_time
        }
    
    def __repr__(self):
        return f'<Usuario {self.usuario_registro}>'

class HistorialTiempos(db.Model):
    __tablename__ = 'historial_tiempos'
    
    id = db.Column(db.Integer, primary_key=True)
    codigo_time = db.Column(db.String(50), nullable=False)
    tiempo_acumulado = db.Column(db.Time, nullable=False)
    tiempo_transcurrido = db.Column(db.Time, nullable=False)
    tiempo_encargado_usuario = db.Column(db.String(100))
    tiempo_fecha_registro = db.Column(db.DateTime, nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'codigo_time': self.codigo_time,
            'tiempo_acumulado': str(self.tiempo_acumulado) if self.tiempo_acumulado else None,
            'tiempo_transcurrido': str(self.tiempo_transcurrido) if self.tiempo_transcurrido else None,
            'tiempo_encargado_usuario': self.tiempo_encargado_usuario,
            'tiempo_fecha_registro': self.tiempo_fecha_registro.isoformat() if self.tiempo_fecha_registro else None
        }

class HistorialAscensos(db.Model):
    __tablename__ = 'historial_ascensos'
    
    id = db.Column(db.Integer, primary_key=True)
    codigo_time = db.Column(db.String(10))
    rango_actual = db.Column(db.String(50))
    mision_actual = db.Column(db.String(255))
    firma_usuario = db.Column(db.String(10))
    firma_encargado = db.Column(db.String(10))
    estado_ascenso = db.Column(db.String(50))
    fecha_ultimo_ascenso = db.Column(db.DateTime)
    fecha_disponible_ascenso = db.Column(db.DateTime)
    usuario_encargado = db.Column(db.String(100))
    accion = db.Column(db.String(20))
    realizado_por = db.Column(db.String(100))
    fecha_accion = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'codigo_time': self.codigo_time,
            'rango_actual': self.rango_actual,
            'mision_actual': self.mision_actual,
            'firma_usuario': self.firma_usuario,
            'firma_encargado': self.firma_encargado,
            'estado_ascenso': self.estado_ascenso,
            'fecha_ultimo_ascenso': self.fecha_ultimo_ascenso.isoformat() if self.fecha_ultimo_ascenso else None,
            'fecha_disponible_ascenso': self.fecha_disponible_ascenso.isoformat() if self.fecha_disponible_ascenso else None,
            'usuario_encargado': self.usuario_encargado,
            'accion': self.accion,
            'realizado_por': self.realizado_por,
            'fecha_accion': self.fecha_accion.isoformat() if self.fecha_accion else None
        }

class GestionVentas(db.Model):
    __tablename__ = 'gestion_ventas'
    
    venta_id = db.Column(db.Integer, primary_key=True)
    venta_titulo = db.Column(db.String(100), nullable=False)
    venta_compra = db.Column(db.DateTime, nullable=False)
    venta_caducidad = db.Column(db.DateTime, nullable=False)
    venta_estado = db.Column(db.String(20), nullable=False)
    venta_costo = db.Column(db.Numeric(10, 2), nullable=False)
    venta_comprador = db.Column(db.Integer)
    comprador_externo = db.Column(db.String(24))
    venta_encargado = db.Column(db.String(30))
    venta_fecha_compra = db.Column(db.DateTime)
    
    def to_dict(self):
        return {
            'venta_id': self.venta_id,
            'venta_titulo': self.venta_titulo,
            'venta_compra': self.venta_compra.isoformat() if self.venta_compra else None,
            'venta_caducidad': self.venta_caducidad.isoformat() if self.venta_caducidad else None,
            'venta_estado': self.venta_estado,
            'venta_costo': float(self.venta_costo) if self.venta_costo else None,
            'venta_comprador': self.venta_comprador,
            'comprador_externo': self.comprador_externo,
            'venta_encargado': self.venta_encargado,
            'venta_fecha_compra': self.venta_fecha_compra.isoformat() if self.venta_fecha_compra else None
        }

class GestionTiempo(db.Model):
    __tablename__ = 'gestion_tiempo'
    
    tiempo_id = db.Column(db.Integer, primary_key=True)
    codigo_time = db.Column(db.String(5), nullable=False, index=True)
    tiempo_status = db.Column(db.String(30), default='disponible')
    tiempo_restado = db.Column(db.Time, default=time(0, 0, 0))
    tiempo_acumulado = db.Column(db.Time, default=time(0, 0, 0))
    tiempo_transcurrido = db.Column(db.Time, default=time(0, 0, 0))
    tiempo_encargado_usuario = db.Column(db.String(50))
    tiempo_fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    tiempo_iniciado = db.Column(db.Time)
    
    def to_dict(self):
        return {
            'tiempo_id': self.tiempo_id,
            'codigo_time': self.codigo_time,
            'tiempo_status': self.tiempo_status,
            'tiempo_restado': str(self.tiempo_restado) if self.tiempo_restado else None,
            'tiempo_acumulado': str(self.tiempo_acumulado) if self.tiempo_acumulado else None,
            'tiempo_transcurrido': str(self.tiempo_transcurrido) if self.tiempo_transcurrido else None,
            'tiempo_encargado_usuario': self.tiempo_encargado_usuario,
            'tiempo_fecha_registro': self.tiempo_fecha_registro.isoformat() if self.tiempo_fecha_registro else None,
            'tiempo_iniciado': str(self.tiempo_iniciado) if self.tiempo_iniciado else None
        }

class GestionRequisitos(db.Model):
    __tablename__ = 'gestion_requisitos'
    
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(20), nullable=False, index=True)
    requirement_name = db.Column(db.String(255))
    times_as_encargado_count = db.Column(db.Integer, default=0)
    ascensos_as_encargado_count = db.Column(db.Integer, default=0)
    is_completed = db.Column(db.String(50))
    last_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user,
            'requirement_name': self.requirement_name,
            'times_as_encargado_count': self.times_as_encargado_count,
            'ascensos_as_encargado_count': self.ascensos_as_encargado_count,
            'is_completed': self.is_completed,
            'last_updated': self.last_updated.isoformat() if self.last_updated else None
        }

class Ascensos(db.Model):
    __tablename__ = 'ascensos'
    
    ascenso_id = db.Column(db.Integer, primary_key=True)
    codigo_time = db.Column(db.String(5), nullable=False, index=True)
    rango_actual = db.Column(db.String(50), nullable=False)
    mision_actual = db.Column(db.String(255))
    firma_usuario = db.Column(db.String(10))
    firma_encargado = db.Column(db.String(10))
    estado_ascenso = db.Column(db.String(20), default='pendiente')
    fecha_ultimo_ascenso = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_disponible_ascenso = db.Column(db.Time)
    usuario_encargado = db.Column(db.String(50))
    es_recluta = db.Column(db.Boolean, default=False)
    
    def to_dict(self):
        return {
            'ascenso_id': self.ascenso_id,
            'codigo_time': self.codigo_time,
            'rango_actual': self.rango_actual,
            'mision_actual': self.mision_actual,
            'firma_usuario': self.firma_usuario,
            'firma_encargado': self.firma_encargado,
            'estado_ascenso': self.estado_ascenso,
            'fecha_ultimo_ascenso': self.fecha_ultimo_ascenso.isoformat() if self.fecha_ultimo_ascenso else None,
            'fecha_disponible_ascenso': str(self.fecha_disponible_ascenso) if self.fecha_disponible_ascenso else None,
            'usuario_encargado': self.usuario_encargado,
            'es_recluta': self.es_recluta
        }

class GestionNotificaciones(db.Model):
    __tablename__ = 'gestion_notificaciones'
    
    notificacion_id = db.Column(db.Integer, primary_key=True)
    notificacion_mensaje = db.Column(db.String(40), nullable=False)
    notificacion_registro = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, index=True)
    id_encargado = db.Column(db.String(16))
    
    def to_dict(self):
        return {
            'notificacion_id': self.notificacion_id,
            'notificacion_mensaje': self.notificacion_mensaje,
            'notificacion_registro': self.notificacion_registro.isoformat() if self.notificacion_registro else None,
            'usuario_id': self.usuario_id,
            'id_encargado': self.id_encargado
        }

class GestionPagas(db.Model):
    __tablename__ = 'gestion_pagas'
    
    pagas_id = db.Column(db.Integer, primary_key=True)
    pagas_usuario = db.Column(db.String(16), nullable=False)
    pagas_rango = db.Column(db.String(40), nullable=False)
    pagas_recibio = db.Column(db.Integer, nullable=False)
    pagas_motivo = db.Column(db.String(30))
    pagas_completo = db.Column(db.String(40), nullable=False)
    pagas_descripcion = db.Column(db.String(255))
    pagas_fecha_registro = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'pagas_id': self.pagas_id,
            'pagas_usuario': self.pagas_usuario,
            'pagas_rango': self.pagas_rango,
            'pagas_recibio': self.pagas_recibio,
            'pagas_motivo': self.pagas_motivo,
            'pagas_completo': self.pagas_completo,
            'pagas_descripcion': self.pagas_descripcion,
            'pagas_fecha_registro': self.pagas_fecha_registro.isoformat() if self.pagas_fecha_registro else None        }
