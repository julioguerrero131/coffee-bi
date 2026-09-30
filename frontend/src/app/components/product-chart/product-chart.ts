import { Component, OnInit, inject, signal } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { DecimalPipe } from '@angular/common';
import { environment } from '../../../environments/environment';

export interface ProductSales {
  product: string;
  total_sales: number;
  ticket_count: number;
}

export interface ApiResponse<T> {
  status: string;
  data: T;
}

@Component({
  selector: 'app-product-chart',
  imports: [DecimalPipe],
  templateUrl: './product-chart.html'
})
export class ProductChart implements OnInit {
  private http = inject(HttpClient);
  
  salesData = signal<ProductSales[]>([]);
  maxSales = signal<number>(0);
  isLoading = signal<boolean>(true);
  error = signal<string | null>(null);

  ngOnInit() {
    this.loadProductData();
  }

  loadProductData() {
    this.isLoading.set(true);
    
    // Consultar el endpoint usando el año actual
    const currentYear = new Date().getFullYear();
    const url = `${environment.apiUrl}/metrics/sales-by-product?year=${currentYear}`;
    
    this.http.get<ApiResponse<ProductSales[]>>(url)
      .subscribe({
        next: (response) => {
          this.salesData.set(response.data);
          // Obtenemos el máximo para calcular el % de las barras
          const max = Math.max(...response.data.map(d => d.total_sales), 1);
          this.maxSales.set(max);
          this.isLoading.set(false);
        },
        error: (err) => {
          console.error('Error fetching product data:', err);
          this.error.set('No se pudieron cargar los productos.');
          this.isLoading.set(false);
        }
      });
  }
}
