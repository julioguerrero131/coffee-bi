import { Component, OnInit, inject, signal } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { DecimalPipe } from '@angular/common';
import { environment } from '../../../environments/environment';

export interface MonthSales {
  year: number;
  month: number;
  total_sales: number;
  ticket_count: number;
}

export interface ApiResponse<T> {
  status: string;
  data: T;
}

@Component({
  selector: 'app-sales-chart',
  imports: [DecimalPipe],
  templateUrl: './sales-chart.html'
})
export class SalesChart implements OnInit {
  private http = inject(HttpClient);
  
  salesData = signal<MonthSales[]>([]);
  maxSales = signal<number>(0);
  isLoading = signal<boolean>(true);
  error = signal<string | null>(null);

  ngOnInit() {
    this.loadSalesData();
  }

  loadSalesData() {
    this.isLoading.set(true);
    
    // Consultar el endpoint usando el año actual
    const currentYear = new Date().getFullYear();
    const url = `${environment.apiUrl}/metrics/sales-by-month?year=${currentYear}`;
    
    this.http.get<ApiResponse<MonthSales[]>>(url)
      .subscribe({
        next: (response) => {
          this.salesData.set(response.data);
          const max = Math.max(...response.data.map(d => d.total_sales), 1);
          this.maxSales.set(max);
          this.isLoading.set(false);
        },
        error: (err) => {
          console.error('Error fetching sales data:', err);
          this.error.set('No se pudieron cargar las ventas.');
          this.isLoading.set(false);
        }
      });
  }

  getMonthName(month: number): string {
    const months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
    return months[month - 1] || '';
  }
}
