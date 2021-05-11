from django.contrib import admin as a
from .models import Project
class PostAdmin(a.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


a.site.register(Project, PostAdmin)
