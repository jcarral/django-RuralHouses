from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lista/', views.CasasList.as_view(template_name="casas/casa_list.jade"), name='lista'),
    url(r'^nueva/', views.NuevaCasa.as_view(template_name="casas/casa_nueva.jade", success_url='casas/casa_nueva.jade'), name='nuevacasa'),
    url(r'^casa/(?P<pk>[0-9]+)/$', views.CasaDetail.as_view(template_name="casas/casa_detail.jade"), name='detail'),
    url(r'^casa/(?P<pk>[0-9]+)/edit/$', views.CasaUpdate.as_view(template_name="casas/casa_update.jade"), name="casaupdate"),
    url(r'^fav/$', views.gestionar_favoritos, name='favorito'),
    url(r'^nuevaoferta/$', views.crear_oferta, name='nuevaoferta'),
    url(r'^borraroferta/$', views.borrar_oferta, name="borrar"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
