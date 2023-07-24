"""
URL configuration for my_project project.

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
from my_app import views
from django.conf import settings
from django.conf.urls.static import static
         
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
    path('signup/',views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('about_url/',views.about_url,name='about_url'),
    path('client_contact/',views.client_contact,name='client_contact'),
    path('courses_url/',views.courses_url,name='courses_url'),
    path('gallery_images/', views.display_gellery, name = 'gallery_images'),
    path('view_staff/',views.display_staff, name = 'view_staff'),
    # path('showform', views.showform),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)