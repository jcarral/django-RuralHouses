from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.CasasList.as_view(template_name="casas/casa_list.jade"), name='lista'),
    #url(r'^casa/(?P<pk>[0-9]+)/$', views.CasaDetail.as_view(template_name="casas/casa_detail.jade"), name='detail'),
    #url(r'^casa/new', views.new_house, name='nueva')
]
