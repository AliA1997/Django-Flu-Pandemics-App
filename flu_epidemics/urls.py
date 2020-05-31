"""flu_epidemics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from website.views import cities_list, countries_list, city_details, country_details, diseases_list, disease_details, pandemics_list, pandemic_details, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('cities', cities_list, name='cities'),
    path('countries', countries_list, name='countries'),
    path('diseases', diseases_list, name='diseases'),
    path('pandemics', pandemics_list, name='pandemics'),
    path('cities/<int:id>', city_details, name='city details'),
    path('countries/<int:id>', country_details, name='country details'),
    path('diseases/<int:id>', disease_details, name='disease details'),
    path('pandemics/<int:id>', pandemic_details, name='pandemic details')
]
