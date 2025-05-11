from django.contrib import admin
from django.urls import path, include
from recettes.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('recettes/', include('recettes.urls')),
    path('comptes/', include('comptes.urls')),
]