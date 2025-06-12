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
    { path: '/', icon: 'bi-house', label: 'Inicio' },
    { path: '/clientes', icon: 'bi-people', label: 'Clientes' },
    { path: '/servicios', icon: 'bi-briefcase', label: 'Servicios' },
    { path: '/reportes', icon: 'bi-bar-chart', label: 'Reportes' },
    { path: '/configuracion', icon: 'bi-gear', label: 'Configuración' }
  ];
}