from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_task, name='add_task'),
    path('task/<int:pk>/reorder/', views.reorder_task, name='reorder_task'),
    path('task/<int:pk>/delete/', views.delete_task, name='delete_record'),
    path('task/<int:pk>/edit/', views.update_task, name='update_task'),
]
