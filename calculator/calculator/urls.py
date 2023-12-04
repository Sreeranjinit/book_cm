"""
URL configuration for calculator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from operation.views import goodview
from operation.views import HelloWorldView,HelloView,goodview,AddView,subsractview,MulView,DivView,NumberView,leapyearview,large,armstsrong,paliandrome,String,Cirly,greeting,prime,fibonacci,FormView
from operation.views import newView,EmiView,signupView,signinview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',HelloWorldView.as_view()),
    path('home/',HelloView.as_view()),
    path('good/', goodview.as_view()),
    path('add/',AddView.as_view()),
    path('sub/',subsractview.as_view()),
    path('mul/',MulView.as_view()),
    path('div/',DivView.as_view()),
    path('num/',NumberView.as_view()),
    path('year/',leapyearview.as_view()),
    path('large/',large.as_view()),
    path('arm/',armstsrong.as_view()),
    path('pal/',paliandrome.as_view()),
    path('string/',String.as_view()),
    path('cirly/',Cirly.as_view()),
    path('greet/',greeting.as_view()),
    path('prime/',prime.as_view()),
    path('fib/',fibonacci.as_view()),
    path('form/',FormView.as_view()),
    path('new/',newView.as_view()),
    path('emi/',EmiView.as_view()),
    path('signup/',signupView.as_view()),
    path('signin/',signinview.as_view())
]
