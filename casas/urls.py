from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lista', views.CasasList.as_view(template_name="casas/casa_list.jade"), name='lista'),
    url(r'^login', views.user_login, name='login'),
    url(r'^logout', views.user_logout, name='logout'),
    url(r'^register', views.registrar_usuario, name='registro'),
    url(r'^modificar/(?P<pk>[0-9]+)/', views.UsuarioUpdate.as_view(template_name="casas/update_user.jade"), name='editarperfil'),
    url(r'^nueva', views.nueva_casa, name='nuevacasa'),
    url(r'^casa/(?P<pk>[0-9]+)/$', views.CasaDetail.as_view(template_name="casas/casa_detail.jade"), name='detail'),

    #url(r'^casa/(?P<pk>[0-9]+)/$', views.CasaDetail.as_view(template_name="casas/casa_detail.jade"), name='detail'),
    #url(r'^casa/new', views.new_house, name='nueva')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
