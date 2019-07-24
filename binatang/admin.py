from django.contrib import admin
from .models import Binatang

# Register your models here.
class BinatangAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'umur']
    list_display_links = ['id', 'nama']

admin.site.register(Binatang, BinatangAdmin)
