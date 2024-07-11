from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   #api to post a comment
   path('postComment', views.postComment, name="postComment"),
   path('',views.blogHome, name='blogHome'),
   path('<str:slug>',views.blogPost,name='blogPost'),
    path('post/<str:slug>/', views.post_detail, name='post_detail'),
]