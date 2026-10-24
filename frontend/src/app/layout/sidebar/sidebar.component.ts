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
    { path: '/', icon: 'bi-house-door-fill', label: 'Inicio' },
    { path: '/informacion', icon: 'bi-info-circle-fill', label: 'Informacion' },
    { path: '/login', icon: 'bi-person-circle', label: 'Iniciar sesión' }, 
    { path: '/registre', icon: 'bi-person-plus-fill', label: 'Registrarse' }
  ];
}