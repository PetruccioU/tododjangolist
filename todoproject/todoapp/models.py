import datetime

from django.db import models
from django.urls import reverse
# python manage.py sqlmigrate todoapp 0002
class TodoListItem(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    start_date = models.DateTimeField(default=datetime.datetime.now)
    update_date = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_done = models.BooleanField(default=False)
    cat= models.ForeignKey('Category', on_delete=models.PROTECT,null=True)

    def __str__(self):
        return self.title

# For dynamic URL use get_absolute_url.
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


