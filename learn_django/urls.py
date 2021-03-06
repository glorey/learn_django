"""learn_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from learn import views as learn_views
from calc import views as calc_views
from learn_template import views as learn_template_views
from learn_template2 import views as learn_template2_views
import learn_template2

urlpatterns = [
    url(r'^$', learn_views.index),
    
    url(r'^add/$', calc_views.add, name='add'),
    url(r'^add2/(\d+)/(\d+)/$', calc_views.add2, name='add2'),
    
    url(r'^learn_template$', learn_template_views.home, name='home'),
    url(r'^learn_template2$', learn_template2_views.home, name='learn_template2'),
    url(r'^loop$', learn_template2_views.loop),
    url(r'^dict$', learn_template2_views.test_dict),
    
    url(r'^admin/', admin.site.urls),
]
