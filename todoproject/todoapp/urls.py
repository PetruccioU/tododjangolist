from django.contrib import admin
from django.urls import path, re_path
from .views import deleteTodoView, archive, AboutForm
from .views import getYourTodoDone, DoneList, MotivationForm, addForm

from .views import *

urlpatterns = [

    path('', todoView.as_view(), name='home'),  # todoView.as_view() - call of function only
    path('donelist/', DoneList, name='donelist'),
    path('motivation/', MotivationForm, name='motivation'),
    path('about/', AboutForm, name='about'),
    path('add/', addForm.as_view(), name='add'),
    #path('addTodoView/',addTodoView),

    path('deleteTodoItem/<slug:post_slug>/', deleteTodoView),
    path('YourTodoDone/<slug:post_slug>/', getYourTodoDone),
#<int:i>
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),

    path('post/<slug:post_slug>/', showPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', showcatView.as_view(), name='category'),

]

#path('post/<int:post_id>/', show_post, name='post'),
#path('category/<int:cat_id>/', show_category, name='category'),


