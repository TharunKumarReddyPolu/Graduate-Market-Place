from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.items, name='items'),
    path('newitem/', views.new_item, name='newitem'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/deleteitem/', views.delete_item, name='deleteitem'),
    path('<int:pk>/edititem/', views.edit_item, name='edititem'),
]