from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [

    path('', TodoView.as_view(), name='home'),  # todoView.as_view() - call of function only
    path('donelist/', DoneList.as_view(), name='donelist'),
    path('add/', AddForm.as_view(), name='add'),

    path('motivation/', MotivationForm.as_view(), name='motivation'),
    path('about/', AboutForm.as_view(), name='about'),

    path('deleteTodoItem/<slug:post_slug>/', delete_todo_view),
    path('YourTodoDone/<slug:post_slug>/', get_your_todo_done),
#<int:i>
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),

    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', ShowCatView.as_view(), name='category'),

    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LogUser.as_view(), name='login'),
    path('logout_user/', LogUser.logout_user),
]

#path('post/<int:post_id>/', show_post, name='post'),
#path('category/<int:cat_id>/', show_category, name='category'),


