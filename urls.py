from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api/products/', views.ProductList.as_view(), name='product-list'),
    path('api/products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('api/transactions/', views.TransactionList.as_view(), name='transaction-list'),
    path('api/transactions/<int:pk>/', views.TransactionDetail.as_view(), name='transaction-detail'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
]
