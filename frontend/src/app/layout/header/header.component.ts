import { Component, EventEmitter, Output } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [
    CommonModule,
    RouterModule
  ],
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent {
  @Output() menuToggle = new EventEmitter<void>();
  
  title = 'Sistema Agencia';
  
  menuItems = [
    {
      id: 'dashboard',
      label: 'Dashboard',
      icon: 'bi-speedometer2',
      children: [
        {
          id: 'home',
          label: 'Inicio',
          icon: 'bi-house',
          path: '/'
        },
        {
          id: 'analytics',
          label: 'Analíticas',
          icon: 'bi-graph-up',
          children: [
            { label: 'Reportes Generales', path: '/analytics/general', icon: 'bi-bar-chart' },
            { label: 'Métricas de Ventas', path: '/analytics/sales', icon: 'bi-currency-dollar' },
            { label: 'Estadísticas de Usuarios', path: '/analytics/users', icon: 'bi-people-fill' }
          ]
        }
      ]
    },
    {
      id: 'clients',
      label: 'Gestión de Clientes',
      icon: 'bi-people',
      children: [
        {
          id: 'client-list',
          label: 'Lista de Clientes',
          icon: 'bi-list-ul',
          path: '/clientes'
        },
        {
          id: 'client-management',
          label: 'Administración',
          icon: 'bi-gear',
          children: [
            { label: 'Nuevo Cliente', path: '/clientes/nuevo', icon: 'bi-person-plus' },
            { label: 'Importar Clientes', path: '/clientes/importar', icon: 'bi-upload' },
            { label: 'Exportar Datos', path: '/clientes/exportar', icon: 'bi-download' }
          ]
        },
        {
          id: 'client-categories',
          label: 'Categorías',
          icon: 'bi-tags',
          children: [
            { label: 'Clientes VIP', path: '/clientes/vip', icon: 'bi-star-fill' },
            { label: 'Clientes Corporativos', path: '/clientes/corporativos', icon: 'bi-building' },
            { label: 'Clientes Individuales', path: '/clientes/individuales', icon: 'bi-person' }
          ]
        }
      ]
    },
    {
      id: 'services',
      label: 'Servicios',
      icon: 'bi-briefcase',
      children: [
        {
          id: 'service-catalog',
          label: 'Catálogo',
          icon: 'bi-grid',
          path: '/servicios'
        },
        {
          id: 'service-types',
          label: 'Tipos de Servicio',
          icon: 'bi-collection',
          children: [
            { label: 'Consultoría', path: '/servicios/consultoria', icon: 'bi-chat-square-text' },
            { label: 'Desarrollo', path: '/servicios/desarrollo', icon: 'bi-code-slash' },
            { label: 'Soporte Técnico', path: '/servicios/soporte', icon: 'bi-tools' }
          ]
        }
      ]
    },
    {
      id: 'reports',
      label: 'Reportes',
      icon: 'bi-bar-chart',
      children: [
        {
          id: 'financial-reports',
          label: 'Reportes Financieros',
          icon: 'bi-currency-dollar',
          children: [
            { label: 'Ingresos Mensuales', path: '/reportes/ingresos', icon: 'bi-graph-up' },
            { label: 'Gastos', path: '/reportes/gastos', icon: 'bi-graph-down' },
            { label: 'Balance General', path: '/reportes/balance', icon: 'bi-calculator' }
          ]
        },
        {
          id: 'operational-reports',
          label: 'Reportes Operacionales',
          icon: 'bi-clipboard-data',
          children: [
            { label: 'Productividad', path: '/reportes/productividad', icon: 'bi-speedometer' },
            { label: 'Proyectos Activos', path: '/reportes/proyectos', icon: 'bi-kanban' },
            { label: 'Tiempo de Respuesta', path: '/reportes/tiempo', icon: 'bi-clock' }
          ]
        }
      ]
    },
    {
      id: 'settings',
      label: 'Configuración',
      icon: 'bi-gear',
      children: [
        {
          id: 'system-config',
          label: 'Sistema',
          icon: 'bi-cpu',
          path: '/configuracion/sistema'
        },
        {
          id: 'user-management',
          label: 'Gestión de Usuarios',
          icon: 'bi-people-fill',
          children: [
            { label: 'Usuarios Activos', path: '/configuracion/usuarios', icon: 'bi-person-check' },
            { label: 'Roles y Permisos', path: '/configuracion/roles', icon: 'bi-shield-check' },
            { label: 'Sesiones', path: '/configuracion/sesiones', icon: 'bi-clock-history' }
          ]
        }
      ]
    },
    {
      id: 'auth',
      label: 'Autenticación',
      icon: 'bi-person-circle',
      children: [
        {
          id: 'login',
          label: 'Iniciar Sesión',
          icon: 'bi-box-arrow-in-right',
          path: '/login'
        },
        {
          id: 'register',
          label: 'Registrarse',
          icon: 'bi-person-plus',
          path: '/registre'
        },
        {
          id: 'info',
          label: 'Información',
          icon: 'bi-info-circle',
          path: '/informacion'
        }
      ]
    }
  ];
}