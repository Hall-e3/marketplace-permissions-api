from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from .renderers import UserListJSONRenderer

User = get_user_model()

class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [UserListJSONRenderer]
    
    def get_queryset(self):
        # Users see other users in their business
        if getattr(self.request.user, 'business', None):
            return User.objects.filter(business=self.request.user.business)
        return User.objects.none()
