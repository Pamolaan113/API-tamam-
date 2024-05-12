from django.contrib import admin
from django.urls import path
from . import views  # Import views from your perabotan app

urlpatterns = [
  path('', views.PerabotList.as_view(), name='perabotan-list'),  # List all furniture
  path('<int:pk>/', views.PerabotDetail.as_view(), name='perabotan-detail'),  # Detail view for specific furniture (by ID)
]


urlpatterns = [
    path('admin/', admin.site.urls),
]
