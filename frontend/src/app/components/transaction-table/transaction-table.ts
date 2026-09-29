import { Component, OnInit, inject, signal } from '@angular/core';
import { DatePipe, DecimalPipe } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';

export interface Transaction {
  _id: string;
  id_ticket: string;
  fecha_hora: string;
  producto: string;
  categoria: string;
  monto: number;
  metodo_pago: string;
  sucursal: string;
}

export interface ApiResponse<T> {
  status: string;
  pagination: {
    total: number;
    skip: number;
    limit: number;
  };
  data: T;
}

@Component({
  selector: 'app-transaction-table',
  imports: [DatePipe, DecimalPipe],
  templateUrl: './transaction-table.html'
})
export class TransactionTable implements OnInit {
  private http = inject(HttpClient);
  
  transactions = signal<Transaction[]>([]);
  isLoading = signal<boolean>(true);
  error = signal<string | null>(null);

  // Pagination state
  limit = signal<number>(5);
  skip = signal<number>(0);
  total = signal<number>(0);

  ngOnInit() {
    this.loadTransactions();
  }

  loadTransactions() {
    this.isLoading.set(true);
    this.error.set(null);
    
    const url = `${environment.apiUrl}/metrics/sales?skip=${this.skip()}&limit=${this.limit()}`;
    
    this.http.get<ApiResponse<Transaction[]>>(url)
      .subscribe({
        next: (response) => {
          this.transactions.set(response.data);
          this.total.set(response.pagination.total);
          this.isLoading.set(false);
        },
        error: (err) => {
          console.error('Error fetching transactions:', err);
          this.error.set('No se pudieron cargar las transacciones. Verifica que el servidor backend esté corriendo.');
          this.isLoading.set(false);
        }
      });
  }

  nextPage() {
    if (this.skip() + this.limit() < this.total()) {
      this.skip.update(v => v + this.limit());
      this.loadTransactions();
    }
  }

  prevPage() {
    if (this.skip() - this.limit() >= 0) {
      this.skip.update(v => v - this.limit());
      this.loadTransactions();
    }
  }

  get currentPage() {
    return Math.floor(this.skip() / this.limit()) + 1;
  }

  get totalPages() {
    return Math.ceil(this.total() / this.limit());
  }
}
