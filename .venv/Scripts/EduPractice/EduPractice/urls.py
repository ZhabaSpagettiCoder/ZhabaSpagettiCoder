"""
URL configuration for EduPractice project.

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
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include
from EduPracticeIDE import views

inclu = [path("Add", views.Add), path("AddSuper", views.AddSuper),path("AddSuper/Server", views.DBAddAdminResponse), path("Add/Server", views.DBAddResponse),path("Info/",views.InfoShow), path("Info/Server",views.Submit),path("Info/Delete/",views.Delete)]
IncludedPattern = [path("incl",views.included), path("noncl",views.noncluded)] #Пустой путь определяется в urlpatterns как основной, он будет отображаться первым
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('main/<int:name>', views.index), #С include работает та же схема, только параметр прописывается раньше дочерней страницы
    #path('uwu/',views.uwu, kwargs={"name":"Sucker","age":"52"}),
    #path('includingTest/', include(IncludedPattern)),
    #path('UwUs/',views.advancedUwU),
    #path('Redirect/',views.redirected),
    #path('Users/',views.CookieThumper),
    #path('Take', views.CookieTaker),
    path('',views.StartPage),
    path('Reg/',views.Registration),
    path('Reg/Server',views.DBRegResponse),
    path('AuthTry',views.AuthTry),
    path('Menu/',views.Menu),
    path('Menu/', include(inclu))
] 