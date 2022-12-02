from django.urls import path
from users import views

app_name='users'
urlpatterns = [
    path('signup/', views.SignupPageView.as_view(), name="signup"),    
]

