from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = 'core_ledger:index'


class CustomLogoutView(LogoutView):
    template_name = 'users/logout.html'
