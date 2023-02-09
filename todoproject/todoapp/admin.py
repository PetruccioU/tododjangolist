from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class TodoListItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_html_photo', 'slug', 'start_date', 'is_done', 'cat', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_published',)
    list_filter = ('is_published', 'start_date')
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'start_date', 'update_date', 'get_html_photo')
    readonly_fields = ('start_date', 'update_date', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")
    # we are not scoping src tags, we are adding filter safe to <img src='{object.photo.url}' width=50>
    get_html_photo.short_description = 'miniatures'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('id', )
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(TodoListItem, TodoListItemAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_header = 'Simple Task Manager Admin'
admin.site.site_title = 'Simple Task Manager'
# Register your models here.
