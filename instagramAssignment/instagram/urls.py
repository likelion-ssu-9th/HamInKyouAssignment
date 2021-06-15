from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('<str:postId>', detail, name="detail"),
    path('new/', new, name="new"),
    path('create/',create, name ="create"),
    path('edit/<str:postId>',edit, name="edit"),
    path('update/<str:postId>', update, name="update"),
    path('delete/<str:postId>', delete, name="delete")
]
