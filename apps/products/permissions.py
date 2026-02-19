from rest_framework import permissions

class HasProductPermission(permissions.BasePermission):
    permission_map = {
        'POST': 'can_create_product',
        'PUT': 'can_edit_product',
        'PATCH': 'can_edit_product',
        'DELETE': 'can_delete_product',
    }
    
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
            
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # For object-level permissions, we need has_object_permission, 
        # but here we check general role permission for the action
        permission_name = self.permission_map.get(request.method)
        if permission_name and request.user.role:
            return getattr(request.user.role, permission_name, False)
            
        return False
        
    def has_object_permission(self, request, view, obj):
        # Ensure object belongs to user's business
        if obj.business != request.user.business:
            return False
            
        return self.has_permission(request, view)
