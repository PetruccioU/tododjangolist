from django.contrib import admin
from django.urls import path, re_path
from .views import todoappView, addTodoView, deleteTodoView, archive
from .views import getYourTodoDone, DoneList

urlpatterns = [

    path('', todoappView, name='home'),
    path('donelist/', DoneList, name='donelist'),
    path('addTodoView/',addTodoView),
    path('deleteTodoItem/<int:i>/', deleteTodoView),
    path('YourTodoDone/<int:i>/', getYourTodoDone),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),

]




