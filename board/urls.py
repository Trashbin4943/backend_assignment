from django.urls import path 
from .views import *

app_name='board'

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('post/create', blog_create, name='blog_create'),
    path('post/detail/<int:pk>', blog_detail, name='blog_detail'),
    path('post/update/<int:pk>',blog_update, name='blog_update'),
    path('post/delete/<int:pk>',blog_delete, name='blog_delete'),
    path('post/comment/create/<int:pk>',comment_create, name='comment_create'),
    path('post/comment/list/<int:pk>',comment_list,name='comment_list')
]