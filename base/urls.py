from django.urls import path
from . import views


urlpatterns = [
    path('', views.endpoints),
    path('advocates/', views.advocates_list, name='advocates'),
    path('advocate_detail/<str:username>/',
         views.AdvocateDetailView.as_view()),
    path('companies/', views.CompanyListView.as_view()),
    # path('advocate_details/<str:username>/',
    #      views.advocate_details, name='advocate_details'),
]
