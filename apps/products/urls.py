from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('<uuid:id>/', views.ProductDetailAPIView.as_view(), name='product-detail'),
    path('<uuid:pk>/approve/', views.approve_product_view, name='product-approve'),
    
    path('public/', views.PublicProductListAPIView.as_view(), name='product-list-public'),
    path('public/<uuid:id>/', views.PublicProductDetailAPIView.as_view(), name='product-detail-public'),
]
