from django_filters import rest_framework as filters
from .models import *


class UserFilter(filters.FilterSet):

    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'created_at', 'is_active', 'is_staff']