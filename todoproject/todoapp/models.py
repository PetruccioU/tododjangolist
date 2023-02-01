import datetime

from django.db import models
from django.urls import reverse
# python manage.py sqlmigrate todoapp 0002
class TodoListItem(models.Model):
    title = models.CharField(max_length=255, verbose_name='Task name:')
    content = models.TextField()
    start_date = models.DateTimeField(default=datetime.datetime.now)
    update_date = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_done = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    cat= models.ForeignKey('Category', on_delete=models.PROTECT,null=True)

    def __str__(self):
        return self.title

# For dynamic URL use get_absolute_url.
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name='Task'
        verbose_name_plural ='Tasks'
        ordering = ['title']

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Categorys:')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Category of task:'
        verbose_name_plural ='Categorys of tasks:'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})