from django.urls import path
from . import views


urlpatterns = [
    path("companies", views.company_list),
    path("users", views.usersCreate),
    path("updateUser", views.updateCompanyusers),
    # path('users/', views.get_users_list, name="users"),
    # path('createUser/', views.create_user, name="create-user"),
]
