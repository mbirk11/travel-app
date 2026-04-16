from django.urls import path
from . import views

urlpatterns = [
    path('', views.trip_list, name='trip_list'),
    path('trip/<int:pk>/', views.trip_detail, name='trip_detail'),
    path('trip/create/', views.trip_create, name='trip_create'),
    path('trip/<int:pk>/edit/', views.trip_update, name='trip_update'),
    path('trip/<int:pk>/delete/', views.trip_delete, name='trip_delete'),
    path('profile/', views.profile_view, name='profile'),
]