from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<str:id>/', views.post, name='post'),
    path('post-detail/<int:id>/', views.post_detail, name='post_detail'), 
]
