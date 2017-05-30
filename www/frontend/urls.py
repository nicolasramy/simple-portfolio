from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^categories/$', views.category_index, name='categories_index'),
    url(r'^categories/(?P<category_slug>\d+)$', views.category_view, name='category_view'),
    url(r'^projects/$', views.project_index, name='projects_index'),
    url(r'^projects/(?P<project_slug>[\w\-]+)/$', views.project_index, name='projects_category_index'),
    url(r'^projects/(?P<project_slug>[\w\-]+)$', views.project_view, name='project_view'),
]
