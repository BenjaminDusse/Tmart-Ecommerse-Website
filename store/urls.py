from django.urls import path
from store import views
from cart import views as cart_views

app_name='store'
urlpatterns = [
    path("", views.home, name="home"),
    path('shop/', views.products, name="products"),
    path('item/<int:id>/',  views.product_detail, name="product_detail"),
]

