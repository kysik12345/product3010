from django.urls import path
from .views import cart_detail

urlpatterns = [
    path('detail/', cart_detail, name="cart_detail"),
    
] 
