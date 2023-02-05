from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='todoHome'),
    path('additem/', views.addTodo, name='addTodo'),
    path('delTodo/<int:id>/', views.delTodo, name='delTodo')
]