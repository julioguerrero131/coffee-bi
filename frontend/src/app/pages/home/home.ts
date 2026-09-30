import { Component } from '@angular/core';
import { DashboardCard } from '../../components/dashboard-card/dashboard-card';
import { TransactionTable } from '../../components/transaction-table/transaction-table';
import { SalesChart } from '../../components/sales-chart/sales-chart';
import { ProductChart } from '../../components/product-chart/product-chart';

@Component({
  selector: 'app-home',
  imports: [DashboardCard, TransactionTable, SalesChart, ProductChart],
  templateUrl: './home.html',
  styleUrl: './home.css'
})
export class Home {
}
