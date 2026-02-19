from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied

from .models import Product
from .serializers import ProductSerializer, ProductCreateSerializer
from .renderers import ProductJSONRenderer, ProductListJSONRenderer
from apps.products.permissions import HasProductPermission

class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProductListJSONRenderer]
    
    def get_queryset(self):

        if getattr(self.request.user, 'business', None):
            return Product.objects.filter(business=self.request.user.business).order_by('-created_at')
        return Product.objects.none()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductCreateSerializer
        return ProductSerializer
    
    def perform_create(self, serializer):
        if not getattr(self.request.user.role, 'can_create_product', False):
            raise PermissionDenied("You don't have permission to create products")
        
        serializer.save(
            business=self.request.user.business,
            created_by=self.request.user
        )

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, HasProductPermission]
    renderer_classes = [ProductJSONRenderer]
    lookup_field = 'id'
    
    def get_queryset(self):
        if getattr(self.request.user, 'business', None):
            return Product.objects.filter(business=self.request.user.business)
        return Product.objects.none()

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def approve_product_view(request, pk):
    # Check permission
    if not getattr(request.user.role, 'can_approve_product', False):
        return Response(
            {"error": "You don't have permission to approve products"},
            status=status.HTTP_403_FORBIDDEN
        )
    
    product = get_object_or_404(Product, id=pk, business=request.user.business)
    product.submit_for_approval()  
    product.approve()
    
    return Response(ProductSerializer(product).data)

class PublicProductListAPIView(generics.ListAPIView):
    queryset = Product.approved.all().order_by('-created_at')
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    renderer_classes = [ProductListJSONRenderer]

class PublicProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.approved.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    renderer_classes = [ProductJSONRenderer]
    lookup_field = 'id'
