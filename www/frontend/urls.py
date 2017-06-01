from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^brands/$', views.brand_index, name='categories_index'),
    url(r'^brands/(?P<brand_slug>[\w\-]+)$', views.brand_view, name='brand_view'),
    url(r'^projects/$', views.project_index, name='projects_index'),
    url(r'^projects/(?P<project_slug>[\w\-]+)$', views.project_view, name='project_view'),
]
