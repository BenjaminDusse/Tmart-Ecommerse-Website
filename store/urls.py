from django.urls import path
from store import views


app_name='store'
urlpatterns = [
    path("", views.home, name="home"),
    path('shop/', views.products, name="products"),
    path('item/<int:pk>/',  views.ProductDetailView.as_view(), name="product_detail"),   
    path("cart/", views.cart, name="cart"),
]