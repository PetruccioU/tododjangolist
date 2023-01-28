from django.contrib import admin
from django.urls import path, re_path
from .views import todoappView, addTodoView, deleteTodoView, archive, AboutForm
from .views import getYourTodoDone, DoneList, showFormForNewTask, MotivationForm

urlpatterns = [

    path('', todoappView, name='home'),
    path('donelist/', DoneList, name='donelist'),
    path('motivation/', MotivationForm, name='motivation'),
    path('about/', AboutForm, name='about'),
    path('add/', showFormForNewTask, name='add'),
    path('addTodoView/',addTodoView),
    path('deleteTodoItem/<int:i>/', deleteTodoView),
    path('YourTodoDone/<int:i>/', getYourTodoDone),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),

]




