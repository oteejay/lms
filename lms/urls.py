"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agents/', include(('agent.urls', 'agent'), namespace='agent')),
    path('clients/', include(('client.urls', 'client'), namespace='client')),
    path('installers/', include(('installer.urls', 'installer'), namespace='installer')),
    path('masters/', include(('master.urls', 'master'), namespace='master')),
    path('personels/', include(('personel.urls', 'personel'), namespace='personel')),
    path('plants/', include(('plant.urls', 'plant'), namespace='plant')),
    path('suppliers/', include(('supplier.urls', 'supplier'), namespace='supplier')),
    path('tanks/', include(('tank.urls', 'tank'), namespace='tank')),
    path('api/', 
        include(([
            path('agents/', include(('agent.api.urls', 'agent'), namespace='agent')),
            path('clients/', include(('client.api.urls', 'client'), namespace='client')),
            path('installers/', include(('installer.api.urls', 'installer'), namespace='installer')),
            path('masters/', include(('master.api.urls', 'master'), namespace='master')),
            path('personels/', include(('personel.api.urls', 'personel'), namespace='personel')),
            path('plants/', include(('plant.api.urls', 'plant'), namespace='plant')),
            path('suppliers/', include(('supplier.api.urls', 'supplier'), namespace='supplier')),
            path('tanks/', include(('tank.api.urls', 'tank'), namespace='tank')),
            path('', include(('temp.api.urls', 'temp'), namespace='temp'))
        ], 'api'), 
        namespace='api')),
    path('/', include(('temp.urls', 'temp'), namespace='temp'))
]
