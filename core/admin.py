from django.contrib import admin
from .models import usuario
# Register your models here.

@admin.register(usuario)
class usuarioadmin(admin.ModelAdmin):
    list_display = ['id', 'address', 'district', 'number', 'city', 'uf', 'zipcode']


   