from django.urls import path
from . import views

app_name = 'core_ledger'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_transaction', views.add_transaction, name='add_transaction'),
    path('add_expense_category/', views.add_expense_category, name='add_expense_category'),
    path('add_income_category/', views.add_income_category, name='add_income_category'),
    path('<int:pk>/transactions/', views.ExpenseCategoryView.as_view(), name='expense_category'),
    path('<int:pk>/incomes/', views.IncomeCategoryView.as_view(), name='income_category'),
    path('transaction/<int:pk>/delete/', views.delete_transaction, name='delete_transaction'),
    path('income/<int:pk>/delete/', views.delete_income, name='delete_income'),
    path('transaction/<int:pk>/', views.TransactionDetailView.as_view(), name='transaction_detail'),
    path('income/<int:pk>/', views.IncomeDetailView.as_view(), name='income_detail'),
    path('transactions/', views.TransactionsView.as_view(), name='transactions'),
    path('incomes/', views.IncomesView.as_view(), name='incomes'),
    path('add_income/', views.add_income, name='add_income'),
]
