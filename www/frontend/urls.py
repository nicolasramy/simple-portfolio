from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^categories/$', views.categories, name='categories_index'),
    url(r'^categories/(?P<category_slug>\d+)$', views.category, name='category_view'),
    url(r'^projects/$', views.projects, name='projects_index'),
    url(r'^projects/(?P<category_slug>\d+)/$', views.projects, name='projects_category_index'),
    url(r'^projects/(?P<project_slug>\d+)$', views.projects, name='projects_view'),
]
