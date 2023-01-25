from django.contrib import admin
from django.urls import path, re_path
from .views import todoappView, addTodoView, deleteTodoView, DoneListView, archive

urlpatterns = [

    path('', todoappView, name='home'),
    path('', DoneListView),
    path('addTodoView/',addTodoView),
    path('deleteTodoItem/<int:i>/', deleteTodoView),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),

]




