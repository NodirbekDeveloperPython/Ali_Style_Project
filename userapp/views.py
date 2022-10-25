from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.models import User


# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, 'page-user-login.html')

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        return redirect('/asosiy/login/')


class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('/')
