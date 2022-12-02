from django.urls import reverse_lazy
from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.views import generic
from users.forms import CustomUserCreationForm

class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'