"""clinica URL Configuration

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
from apps.estetica.views import Home
from django.conf import settings
from django.conf.urls.static import static
#api
from django.conf.urls import url

urlpatterns = [

    path('admin/', admin.site.urls),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('course/', include('course.urls')),
  #  path('estetica/',include(('apps.estetica.urls','estetica'))),
    path('home/',Home, name='index'),
]

#api
urlpatterns += [
    path('api/', include(('apps.estetica.urls', 'estetic'))),

]

urlpatterns += [
    path('api/v1/auth', include(('rest_framework.urls', 'rest_framwork'))),
]
