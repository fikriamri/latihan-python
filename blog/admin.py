from django.contrib import admin
from .models import Blog, Mentee, Mentor
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'judul', 'isi', 'pic', 'tanggal_pembuatan', 'comment']
    list_display_links = ['id', 'judul']
    search_fields = ['judul']

admin.site.register(Blog, BlogAdmin)

class MenteeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'quotes', 'pic']
    list_display_links = ['id', 'nama']
    search_fields = ['nama']

admin.site.register(Mentee, MenteeAdmin)

class MentorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nama', 'quotes', 'pic']
    list_display_links = ['id', 'nama']
    search_fields = ['nama']

admin.site.register(Mentor, MentorAdmin)