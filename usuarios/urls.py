from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^login', views.user_login, name='login'),
    url(r'^logout', views.user_logout, name='logout'),
    url(r'^signup', views.registrar_usuario, name='registro'),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UsuarioFicha.as_view(template_name="usuarios/usuario_detail.jade"), name='fichaUsuario'),
    url(r'^user/(?P<pk>[0-9]+)/edit', views.UsuarioUpdate.as_view(template_name="usuarios/update_user.jade"), name='editarperfil'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
