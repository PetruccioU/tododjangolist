# ========================================================
# import:
from django.db.models import Count
from .models import *
from django.core.cache import cache


# ========================================================
# menu:

menu = [{'title': "All Tasks", 'url_name': 'home'},
        {'title': "Done", 'url_name': 'donelist'},
        {'title': "Add Task", 'url_name': 'add'},
        {'title': "Motivational Quotes", 'url_name': 'motivation'},
        {'title': "About Us", 'url_name': 'about'}
]

# ===========================================================


class DataMixin:
    paginate_by = 3
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = cache.get('cats')
        if not cats:
            cats = Category.objects.annotate(Count('todolistitem'))
            cache.set('cats', cats, 60)
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)
            context['auth'] = False
        else:
            context['auth'] = True
        context['menu'] = user_menu
        context['cats'] = cats
        #context['cat_for_title'] = post.cat
        #if 'cat_selected' not in context:
        #    context['cat_selected'] = 0
        return context
