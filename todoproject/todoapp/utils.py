# ========================================================
# import:
from django.db.models import Count
from .models import *

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
        cats = Category.objects.annotate(Count('todolistitem'))
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)
            context['auth'] = False
        else:
            context['auth'] = True
        #        cats = Category.objects.all()
        #catid = Category.objects.get(slug=self.kwargs['cat_slug'])
        #        context = super().get_context_data(**kwargs)
        #        context['menu'] = menu
        #        context['title'] = 'Category - ' + str(context['posts'][0].cat)
        #context['cat_selected'] = catid.name
        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
