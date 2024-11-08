from django.urls import path
from .views import LaptopListView, LaptopCreateView, LaptopDetailView, LaptopUpdateView, LaptopDeleteView

app_name = "app"

urlpatterns = [
    path('laptops/', LaptopListView.as_view(), name='laptop-list'),
    path('laptops/create/', LaptopCreateView.as_view(), name='laptop-create'),
    path('laptops/<int:pk>/', LaptopDetailView.as_view(), name='laptop-detail'),
    path('laptops/update/<int:pk>/', LaptopUpdateView.as_view(), name='laptop-update'),
    path('laptops/delete/<int:pk>/', LaptopDeleteView.as_view(), name='laptop-delete'),
]