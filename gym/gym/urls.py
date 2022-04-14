"""gym URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import re_path
from django.conf import settings
from app import views
from django.conf.urls.static import static

urlpatterns = [
    re_path('admin/', admin.site.urls),

    re_path(r'^$', views.index, name='index'),
    re_path(r'^SuperAdmin_trainees/$', views.SuperAdmin_trainees, name='SuperAdmin_trainees'),
    re_path(r'^SuperAdmin_ActiveTrainees/$', views.SuperAdmin_ActiveTrainees, name='SuperAdmin_ActiveTrainees'),
    re_path(r'^SuperAdmin_PassiveTrainees/$', views.SuperAdmin_PassiveTrainees, name='SuperAdmin_PassiveTrainees'),
    re_path(r'^SuperAdmin_ActiveTraineeProfile/$', views.SuperAdmin_ActiveTraineeProfile, name='SuperAdmin_ActiveTraineeProfile'),
    re_path(r'^SuperAdmin_PassiveTraineeProfile/$', views.SuperAdmin_PassiveTraineeProfile, name='SuperAdmin_PassiveTraineeProfile'),
    re_path(r'^SuperAdmin_Machines/$', views.SuperAdmin_Machines, name='SuperAdmin_Machines'),
    re_path(r'^SperAdmin_dumbell/$', views.SperAdmin_dumbell, name='SperAdmin_dumbell'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)