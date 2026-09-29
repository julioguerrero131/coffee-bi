import { Component, input } from '@angular/core';

@Component({
  selector: 'app-dashboard-card',
  imports: [],
  templateUrl: './dashboard-card.html'
})
export class DashboardCard {
  // En Angular 19+ podemos usar la señal input() que es el equivalente a las props de React
  title = input<string>('');
}
