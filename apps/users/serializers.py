from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

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
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'business', 'role']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
