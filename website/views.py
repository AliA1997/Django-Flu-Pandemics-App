from django.shortcuts import render, get_object_or_404, get_list_or_404
from countries.models import City, Country
from pandemics.models import Disease, Pandemic

# Create your views here.


def home(request):
    return render(request, 'website/home.html');


def cities_list(request):
    cities = City.objects.all()
    return render(request, 'website/cities_list.html', {"cities": cities})


def countries_list(request):
    countries = Country.objects.all()
    return render(request, 'website/countries_list.html', {"countries": countries })


def city_details(request, id):
    city = get_object_or_404(City, pk=id)
    return render(request, 'website/city_details.html', {"city": city})


def country_details(request, id):
    country = get_object_or_404(Country, pk=id)
    return render(request, 'website/country_details.html', {"country": country})


def diseases_list(request):
    diseases = Disease.objects.all()
    return render(request, 'website/diseases_list.html', {"diseases": diseases})


def pandemics_list(request):
    pandemics = Pandemic.objects.all()
    return render(request, 'website/pandemics_list.html', {"pandemics": pandemics})


def disease_details(request, id):
    disease = get_object_or_404(Disease, pk=id)
    return render(request, 'website/disease_details.html', {"disease": disease})


def pandemic_details(request, id):
    pandemic = get_object_or_404(Pandemic, pk=id)
    return render(request, 'website/pandemic_details.html', {"pandemic": pandemic})