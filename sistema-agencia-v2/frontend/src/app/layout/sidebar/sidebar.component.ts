import { Component, Input } from '@angular/core';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatListModule } from '@angular/material/list';
import { MatIconModule } from '@angular/material/icon';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-sidebar',
  standalone: true,
  imports: [
    CommonModule,
    RouterModule,
    MatSidenavModule,
    MatListModule,
    MatIconModule
  ],
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.scss']
})
export class SidebarComponent {
  @Input() opened = true;
  
  menuItems = [
    { path: '/', icon: 'home', label: 'Inicio' },
    { path: '/clientes', icon: 'people', label: 'Clientes' },
    { path: '/servicios', icon: 'business_center', label: 'Servicios' },
    { path: '/reportes', icon: 'assessment', label: 'Reportes' },
    { path: '/configuracion', icon: 'settings', label: 'Configuración' }
  ];
}