"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.auth import views as auth_v
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from users import views as user_view
from llinked import views as llinked_view

urlpatterns = [
    path('', include('llinked.urls')),
    path('', llinked_view.index, name='home'),
    path('about/', llinked_view.about, name='about'),
    path('register/', user_view.register, name='register'),
    path('login/', auth_v.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_v.LogoutView.as_view(template_name='users/logout.html'), name='logout'),\
    path('profile/', user_view.profile, name='profile'),
    path('profile/update', user_view.update, name='update'),
    path('admin/', admin.site.urls)
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
