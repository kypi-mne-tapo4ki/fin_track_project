from django.urls import path
from . import views

app_name = 'core_ledger'

urlpatterns = [
    path('', views.index, name='index'),
    #  add URLs
    path('add_category/', views.add_category, name='add_category'),
    path('add_operation/', views.add_operation, name='add_operation'),
    path('add_tag/', views.add_tag, name='add_tag'),
    #  single object URLs
    path('category/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('operation/<int:pk>/', views.OperationDetailView.as_view(), name='operation'),
    path('tag/<int:pk>/', views.TagDetailView.as_view(), name='tag'),
    #  sets of objects URLs
    path('operations/', views.OperationsView.as_view(), name='operations'),
    #  delete URLs
    path('category/<int:pk>/delete/', views.delete_category, name='delete_category'),
    path('operation/<int:pk>/delete/', views.delete_operation, name='delete_operation'),
    path('tag/<int:pk>/delete/', views.delete_tag, name='delete_tag'),
]
