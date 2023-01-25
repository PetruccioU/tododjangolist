import datetime

from django.db import models

class TodoListItem(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    start_date = models.DateTimeField(default=datetime.datetime.now)
    update_date = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_done = models.BooleanField(default=False)

# Create your models here.







