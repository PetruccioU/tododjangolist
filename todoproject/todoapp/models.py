import datetime

from django.db import models

class TodoListItem(models.Model):
    content = models.TextField()
    start_date = models.DateTimeField(default=datetime.datetime.now)
    is_done = models.BooleanField(default=False)
# Create your models here.







