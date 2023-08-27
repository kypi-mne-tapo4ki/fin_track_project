from django.urls import path
from . import views

app_name = 'core_ledger'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_transaction', views.add_transaction, name='add_transaction'),
    path('add_expense_category/', views.add_expense_category, name='add_expense_category'),
    path('add_income/', views.add_income, name='add_income'),
    path('<int:pk>/transactions/', views.CategoryTransactionsView.as_view(), name='category_transactions'),
    path('transaction/<int:pk>/delete/', views.delete_transaction, name='delete_transaction'),
]
