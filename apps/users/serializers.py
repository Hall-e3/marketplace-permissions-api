from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

from apps.businesses.models import Business
from apps.roles.models import Role

class UserSerializer(serializers.ModelSerializer):
    business_name = serializers.CharField(source='business.name', read_only=True)
    role_name = serializers.CharField(source='role.name', read_only=True)
    permissions = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = [
            'id', 'email', 'first_name', 'last_name', 
            'business', 'business_name', 'role', 'role_name',
            'permissions', 'date_joined'
        ]
        read_only_fields = ['id', 'date_joined']
        
    def get_permissions(self, obj):
        if not obj.role:
            return {}
        return {
            'can_create_product': obj.role.can_create_product,
            'can_edit_product': obj.role.can_edit_product,
            'can_approve_product': obj.role.can_approve_product,
            'can_delete_product': obj.role.can_delete_product,
        }

class CreateUserSerializer(serializers.ModelSerializer):
    business_name = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'business_name']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        business_name = validated_data.pop('business_name')
        password = validated_data.pop('password')
        
        # Create business
        business, _ = Business.objects.get_or_create(name=business_name)
        
        # Get or create default admin role
        role, _ = Role.objects.get_or_create(
            name=Role.RoleType.ADMIN,
            defaults={
                'can_create_product': True,
                'can_edit_product': True,
                'can_approve_product': True,
                'can_delete_product': True,
            }
        )
        
        user = User.objects.create_user(
            email=validated_data['email'],
            password=password,
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            business=business,
            role=role
        )
        return user
