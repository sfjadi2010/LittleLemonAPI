from django.urls import path
from . import views

urlpatterns = [
    path('menu_items/', views.menu_items),
    path('menu_items/<str:pk>/', views.single_item),
    path('category/<int:pk>/', views.category_detail, name='category_detail')
]
