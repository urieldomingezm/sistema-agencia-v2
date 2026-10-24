import { Component, HostListener } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-footer',
  standalone: true,
  imports: [
    CommonModule
  ],
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.scss']
})
export class FooterComponent {
  currentYear = new Date().getFullYear();
  showScrollButton = false;
  
  @HostListener('window:scroll')
  onWindowScroll() {
    // Mostrar el botón cuando el usuario ha desplazado más de 300px
    this.showScrollButton = window.scrollY > 300;
  }
  
  scrollToTop() {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  }
}