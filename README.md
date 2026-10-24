<div align="center">

# 🏢 Sistema de Gestión de Agencia · v2

API REST en Flask + frontend en Angular para administrar una agencia de Habbo.
Es la migración de la [versión original en PHP](https://github.com/urieldomingezm/Sistema_agencia) a una arquitectura separada por capas.

![Python](https://img.shields.io/badge/Python_3.9-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![Angular](https://img.shields.io/badge/Angular_19-DD0031?style=flat-square&logo=angular&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL_16-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![License](https://img.shields.io/badge/licencia-MIT-green?style=flat-square)

</div>

## ✨ Qué cambia respecto a la v1

| v1 (PHP) | v2 |
|---|---|
| Vistas y lógica mezcladas en PHP | API REST (Flask) + SPA (Angular) separadas |
| MySQL con SQL directo | PostgreSQL con SQLAlchemy (ORM) |
| Lógica en scripts sueltos | Capas: `routes` → `services` → `database` |

## 🧱 Arquitectura

```
Angular (SPA) ──HTTP/JSON──▶ Flask API ──SQLAlchemy──▶ PostgreSQL
   :8080                        :5000                      :5432
```

## 📁 Estructura

```
.
├── backend/
│   ├── app.py              # Fábrica de la app Flask
│   ├── config.py           # Configuración por entorno
│   ├── database/           # Conexión y modelos SQLAlchemy
│   ├── routes/             # Endpoints (blueprints) por módulo
│   ├── services/           # Lógica de negocio
│   └── requirements.txt
├── frontend/
│   └── src/app/
│       ├── layout/         # Header, sidebar, footer
│       └── pages/          # Home, login, registro
├── docker-compose.yml
└── .env.example
```

## 🔌 API

| Módulo | Prefijo |
|---|---|
| Autenticación | `/api/auth` |
| Usuarios | `/api/users` |
| Administración | `/api/admin` |
| Ascensos / historial | `/api/ascensos`, `/api/historial-ascensos` |
| Tiempos / historial | `/api/gestion-tiempo`, `/api/historial-tiempos` |
| Ventas | `/api/gestion-ventas` |
| Pagas | `/api/gestion-pagas` |
| Requisitos | `/api/gestion-requisitos` |
| Notificaciones | `/api/gestion-notificaciones` |
| Health check | `/health` |

## 🚀 Instalación

**Requisitos:** Docker y Docker Compose.

```bash
git clone https://github.com/urieldomingezm/sistema-agencia-v2.git
cd sistema-agencia-v2
cp .env.example .env        # cambia SECRET_KEY y la contraseña
docker compose up --build -d
```

| Servicio | URL |
|---|---|
| Frontend | http://localhost:8080 |
| API | http://localhost:5000 |

### Desarrollo sin Docker

```bash
# Backend
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
export DATABASE_URL=postgresql://postgres:tu_contraseña@localhost:5432/agencia_habbo
python app.py

# Frontend
cd frontend
npm install
npm start                   # http://localhost:4200
```

## 🔐 Variables de entorno

| Variable | Descripción |
|---|---|
| `FLASK_ENV` | `development` o `production` |
| `SECRET_KEY` | Clave para firmar sesiones y tokens |
| `POSTGRES_USER` / `POSTGRES_PASSWORD` / `POSTGRES_DB` | Credenciales de PostgreSQL |

## 🗺️ Pendientes

- [ ] Completar las vistas de Angular para todos los módulos de la API
- [ ] Migraciones con Flask-Migrate en lugar de `create_tables()`
- [ ] Tests del backend

## 👤 Autor

**Angel Uriel Domínguez Medina** · [GitHub](https://github.com/urieldomingezm) · [Portafolio](https://cv-uriel-nine.vercel.app/)

## 📄 Licencia

Distribuido bajo la licencia MIT. Consulta [LICENSE](LICENSE).
