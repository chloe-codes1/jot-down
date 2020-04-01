from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new_review/', views.new_review),
    path('create_review/', views.create_review),
    path('review_detail/<int:pk>/', views.review_detail),
    path('delete_review/<int:pk>/', views.delete_review),
    path('update_review/<int:pk>', views.update_review),
    path('search/', views.search),
    ]