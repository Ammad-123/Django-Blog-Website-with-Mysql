from django.urls import path
from .views import create_post,post_list,post_detail,home_page

urlpatterns = [
    path('', home_page, name='home_page'),
    path('create_post/', create_post, name='create_post'),
    path('posts/<slug:slug>/', post_detail, name='post_detail'),
    path('posts/', post_list, name='post_list'),

]
