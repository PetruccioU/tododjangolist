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