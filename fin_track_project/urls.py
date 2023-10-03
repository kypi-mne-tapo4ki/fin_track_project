from django.contrib import admin
from django.urls import include, path
from core_ledger import views


urlpatterns = [
    path('', views.home, name='home'),
    path("core_ledger/", include("core_ledger.urls")),
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls', namespace='auth')),

]
