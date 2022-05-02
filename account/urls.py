from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='api_login'),
    path('create/', UserCreateView.as_view(), name='api_create_user'),
    path('update/', UserUpdateView.as_view(), name='api_update_user'),
    path('users/', UserView.as_view(), name='api_users_list'),
    path('search/', UserSearchView.as_view(), name='api_users_search'),
]