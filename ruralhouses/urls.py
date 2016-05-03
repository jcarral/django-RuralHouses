from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('casas.urls', namespace='casas')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    
]
