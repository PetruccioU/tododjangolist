from django import template
from todoapp.models import *

register = template.Library()

@register.simple_tag(name='get_cats')
def get_categories():
    return Category.objects.all()





