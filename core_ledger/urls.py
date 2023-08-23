from django.urls import path
from . import views

app_name = 'core_ledger'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_transaction', views.add_transaction, name='add_transaction'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_income/', views.add_income, name='add_income'),
]
