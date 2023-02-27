from django.contrib import admin
from django.urls import path,include
from blog import views 
from home import views as hviews

urlpatterns = [
   
    path('postcomment/', views.postcomment,name='postcomment'),
    path('', views.bloghome,name='bloghome'),
    path('<str:slug>', views.blogpost,name='blogpost'),
    path('logout/',hviews.handlelogout,name="handlelogout"),

    # API to post comment
]