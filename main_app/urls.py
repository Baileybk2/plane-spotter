from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('planes/', views.plane_index, name='plane-index'),
    path('planes/<int:plane_id>/', views.plane_detail, name='plane-detail'),
    path('planes/create/', views.PlaneCreate.as_view(), name='plane-create')
]