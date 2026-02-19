from django.urls import path
from . import views

urlpatterns = [
    # Internal routes
    path('', views.ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('<uuid:id>/', views.ProductDetailAPIView.as_view(), name='product-detail'),
    path('<uuid:pk>/approve/', views.approve_product_view, name='product-approve'),
    
    # Public routes
    # public/ prefix handled in main urls.py usually, but if grouped here:
    # We'll expose public views here too or via a separate 'public/' include
]
