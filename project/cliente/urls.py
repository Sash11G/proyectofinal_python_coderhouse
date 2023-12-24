from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


app_name = "cliente"

urlpatterns = [
    path('', views.home, name="index"),
    #### BLOG ####
    path('create_blog_post/', views.create_blog_post, name='blogpost-create'),
    path('blogposts/', views.blogpost_list, name='blogpost-list'),
    path('blogposts/<int:pk>/', views.BlogPostDetailView.as_view(), name='blogpost-detail'),
    path('blogposts/<int:pk>/update/', views.BlogPostUpdateView.as_view(), name='blogpost-update'),



    
    
]
    
    
    
