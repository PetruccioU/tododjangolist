from django.contrib import admin
from django.urls import path, re_path
from .views import todoappView, addTodoView, deleteTodoView, archive, AboutForm
from .views import getYourTodoDone, DoneList, showFormForNewTask, MotivationForm
from .views import Technical_problem, Analysis_task, HR_task, Management_task, Marketing_task, Self_motivation_task

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
    path('techproblem/', Technical_problem, name='techproblem'),
    path('analyse/', Analysis_task, name='analyse'),
    path('hrtask/', HR_task, name='hrtask'),
    path('management/', Management_task, name='management'),
    path('marketing/', Marketing_task, name='marketing'),
    path('selfmotivation/', Self_motivation_task, name='selfmotivation'),

]




