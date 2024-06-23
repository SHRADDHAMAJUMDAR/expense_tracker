"""
URL configuration for consumeapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getdata/', views.get_api_data, name='get-data'),
    path('postdata/', views.do_post_data, name='post-data'),
    path('putdata/<int:cat_id>/', views.do_put_data, name='edit-cat'),
    path('deldata/<int:cat_id>/', views.do_delete_data, name='del-cat'),
    path('getact/', views.getactdata, name='get-act'),
    path('saveact/', views.saveactdata, name='save-act'),
    # path('home/', views.home, name='home'),
    # path('', include('getpost.url_getpost'))
    
]
