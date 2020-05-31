from django.contrib import admin
from countries.models import Country, City, Religion
from pandemics.models import Disease, Pandemic

# Register your models here.
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Religion)
admin.site.register(Disease)
admin.site.register(Pandemic)