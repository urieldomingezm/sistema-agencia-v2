import { Component, Input } from '@angular/core';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-sidebar',
  standalone: true,
  imports: [
    CommonModule,
    RouterModule
  ],
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.scss']
})
export class SidebarComponent {
  @Input() opened = true;
  
  menuItems = [
    { path: '/', icon: 'bi-house', label: 'Inicio' },
    { path: '/clientes', icon: 'bi-people', label: 'Clientes' },
    { path: '/servicios', icon: 'bi-briefcase', label: 'Servicios' },
    { path: '/reportes', icon: 'bi-bar-chart', label: 'Reportes' },
    { path: '/configuracion', icon: 'bi-gear', label: 'Configuración' }
  ];
}