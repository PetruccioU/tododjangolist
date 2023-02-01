from django.contrib import admin
from django.urls import path, re_path
from .views import todoappView, deleteTodoView, archive, AboutForm
from .views import getYourTodoDone, DoneList, showFormForNewTask, MotivationForm

from .views import *

urlpatterns = [

    path('', todoappView, name='home'),
    path('donelist/', DoneList, name='donelist'),
    path('motivation/', MotivationForm, name='motivation'),
    path('about/', AboutForm, name='about'),
    path('add/', showFormForNewTask, name='add'),
    #path('addTodoView/',addTodoView),

    path('deleteTodoItem/<int:i>/', deleteTodoView),
    path('YourTodoDone/<int:i>/', getYourTodoDone),

    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),

    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),


]




