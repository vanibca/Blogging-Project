from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    #path('<slug:title>/', views.PostDetail.as_view(), name='post_detail'),
]