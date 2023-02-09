"""ainun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.conf.urls.static import static
from django.conf import settings

# from rofiq.admin import rofiq_admin_site

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('entity-admin/', admin.site.urls),
    # path('rofiq-admin/', rofiq_admin_site.urls),
    path('', include('rofiq.urls'))
    
]
admin.site.site_header = "Rofiq Login"
admin.site.site_title = "Rofiq Admin Portal"
admin.site.index_title = "Welcome to Rofiq Researcher Portal"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

