from django.urls import path

from .views import RegistrationAPIView

app_name = 'authentication'
urlpatterns = [
    path('', RegistrationAPIView.as_view()),
]
