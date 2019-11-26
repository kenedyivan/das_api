from django.contrib import admin

# Register your models here.
from api.models import District, SubCounty

admin.site.register(District)
admin.site.register(SubCounty)
