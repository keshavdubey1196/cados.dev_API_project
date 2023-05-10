from django.urls import path
from . import views


urlpatterns = [
    path('', views.endpoints),
    path('advocates/', views.advocates_list),
    path('advocate_details/<str:username>/', views.advocate_details),
]
