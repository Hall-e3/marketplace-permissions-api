from django.urls import path, include
from .views import UserListAPIView

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user-list'),
]
