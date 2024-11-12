from django.urls import path, include
from rest_framework.routers import DefaultRouter
from store import views


router = DefaultRouter()
router.register(r'orders', views.OrderViewSet, basename='order')


urlpatterns = [
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('products/', views.ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('orders/create/', views.CreateOrderView.as_view(), name='order-create'),
    path('', include(router.urls)),
]
