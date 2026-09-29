import { Component } from '@angular/core';
import { DashboardCard } from '../../components/dashboard-card/dashboard-card';
import { TransactionTable } from '../../components/transaction-table/transaction-table';

@Component({
  selector: 'app-home',
  imports: [DashboardCard, TransactionTable],
  templateUrl: './home.html',
  styleUrl: './home.css'
})
export class Home {
}
