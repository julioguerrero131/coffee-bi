import { Component } from '@angular/core';
import { DashboardCard } from '../../components/dashboard-card/dashboard-card';
import { TransactionTable } from '../../components/transaction-table/transaction-table';
import { SalesChart } from '../../components/sales-chart/sales-chart';

@Component({
  selector: 'app-home',
  imports: [DashboardCard, TransactionTable, SalesChart],
  templateUrl: './home.html',
  styleUrl: './home.css'
})
export class Home {
}
