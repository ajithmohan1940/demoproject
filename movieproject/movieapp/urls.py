from django.contrib import admin
from django.urls import path, include
from . import views

app_name='movieapp'

urlpatterns = [
    path('',views.index,name='views'),
    path('movie/<int:mid>/',views.details,name='details'),
    path('add/',views.add,name='add_movie'),
    path('edit/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]
