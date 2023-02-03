from django.contrib import admin
from .models import *

class TodoListItemAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug' ,'start_date','is_done','cat','is_published')
    list_display_links = ('id','title')
    search_fields = ('title','content')
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('id', )
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(TodoListItem, TodoListItemAdmin)
admin.site.register(Category, CategoryAdmin)


# Register your models here.
