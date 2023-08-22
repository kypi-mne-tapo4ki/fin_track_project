from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from core_ledger import views



urlpatterns = [
    path("core_ledger/", include("core_ledger.urls")),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('register/', views.register, name='register'),
]
