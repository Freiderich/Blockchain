"""
URL configuration for Blockchain project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from myapp import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.users_page, name="users"), 
    path("users/", views.users_page, name="users_page"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/logout/", LogoutView.as_view(template_name="registration/logout.html"), name="logout"),

]
from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.users_page, name="users"), 
    path("users/", views.users_page, name="users_page"),

    # ✅ Custom logout MUST come BEFORE the include
    path("accounts/logout/", LogoutView.as_view(template_name="registration/logout.html"), name="logout"),

    # Default auth routes (login, password reset, etc.)
    path("accounts/", include("django.contrib.auth.urls")),
]
