import datetime

from django.db import models
from django.urls import reverse
# python manage.py sqlmigrate todoapp 0002
class TodoListItem(models.Model):
    title = models.CharField(max_length=255, verbose_name='Task name:')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL:")
    content = models.TextField(blank=True, verbose_name="Text of task:")
    start_date = models.DateTimeField(auto_now_add=True, verbose_name="Time of creation:")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Time of update:")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_done = models.BooleanField(default=False,verbose_name="Is Done:")
    is_published = models.BooleanField(default=True, verbose_name="Published:")
    cat= models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Category:")
    # ORM tip: add parameter related_name = 'get_posts' to 'cat' field, to use
    # this name in query instead of using: <secondary_model>_set, for connected model.

    # ORM ORM ORM ORM ORM ORM ORM ORM ORM ORM ORM ORM ORM ORM ORM ORM ORM ORM ORM:
    # c=Category.objects.get(pk=1)
    # c.TodoListItem_set.all() # all items with cat=1
    # equal to c.get_posts_set.all() # if we add ,related_name = 'get_posts'
    # TodoListItem.object.filter(pk__in[1,3,6,9], is_published=True)  # AND logic
    # TodoListItem.object.filter(cat__in[1,2])

    # from django.db.models import Q   # to use OR XOR NOR
    # TodoListItem.object.filter(Q(cat_id_in[1,2]) | Q(pk__lt=5)) # OR logic priority 3
    # TodoListItem.object.filter(Q(cat_id_in[1,2]) & Q(pk__lt=5)) # AND logic priority 2
    # TodoListItem.object.filter(~Q(cat_id_in[1,2]) & Q(pk__lt=5))
    # ~Q(cat_id_in[1,2]) - NOT(Q(cat_id_in[1,2])) # logic, priority 1
    # TodoListItem.object.order_by('pk').first
    # TodoListItem.object.latest('time_update')
    # w.get_previous_by_time_update()  (w.get_previous_by_<field_name>())
    # w.get_previous_by_time_update(pk__gt=10)

    # c2=Category.objects.get(pk=3)
    # c2.TodoListItem_set.exists()
    # c2.TodoListItem_set.count()
    # TodoListItem.object.filter(cat__slug='HR tasks').count()
    # TodoListItem.object.filter(cat__name='HR tasks')  = INNER JOIN of TodoListItem and Categories
    # TodoListItem.object.filter(cat__name__contains='HR')
    # Category.objects.filter(TodoListItem__title__contains='HR')
    # (or maybe instead of TodoListItem use name preselected in the shell)

    # aggregation: from django.db.models import *
    # TodoListItem.object.aggregate(Min('cat_id'), Max('cat_id'))  # dictionary in result
    # TodoListItem.object.aggregate(cat_min=Min('cat_id'), cat_max=Max('cat_id'))
    # TodoListItem.object.aggregate(res=Sum('cat_id') - Count('cat_id')), {'res':<>}
    # TodoListItem.object.filter(cat__name__contains='abc').aggregate(Min('cat_id'), Max('cat_id'))
    # TodoListItem.object.values('title', 'cat_id'),get(pk=1)
    # TodoListItem.object.values('title', 'cat__name'),get(pk=1)  # cat__name from Category with INNER JOIN on SQL

    # .values + annotate = GROUP BY :
    # TodoListItem.object.values('cat_id').annotate(Count('id'))
    # but you have to comment on the 'ordering' parameter on class Meta
    # for TodoListItem Model
    # Or another usage of annotate:
    # c3=Category.objects.annotate(Count('TodoListItem'))
    # c3[0].TodoListItem__count # this will show a number of items in firs category
    # c4=Category.objects.annotate(total=Count('TodoListItem'))
    # c4[0].total # show the same as previous
    # c5=Category.objects.annotate(total=Count('TodoListItem')).filter(total__gt=0)
    # c5 #will show the categories which have non-zero number of records

    # from django.db.models import F   # class F
    # TodoListItem.object.filter(pk__gt=F('cat_id')) # gain all records with pk greater than cat_id:)
    # To count how much times the page is viewed(field views stores the number of
    # times when the page('abc') is viewed by users):
    # TodoListItem.object.filter(slug='abc').update(views=F('views')+1)  # plus 1 view
    # or:
    # w=TodoListItem.object.get(pk=1)
    # w.views=F('views')+1
    # w.save()     # the same

    # Database Functions:
    # ps=TodoListItem.object.annotate(len=length('title'))
    # for i in ps:
    # print(i.title, i.len)

    # RAW SQL:
    # TodoListItem.object.raw('SELECT * FROM TodoListItem')
    #


    def __str__(self):
        return self.title

# For dynamic URL use get_absolute_url.
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name='Task'
        verbose_name_plural ='Tasks'
        ordering = ['title']



class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Categories:')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL:")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Category of task:'
        verbose_name_plural ='Categorys of tasks:'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})