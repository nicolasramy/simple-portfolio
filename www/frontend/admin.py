# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Parameter, Brand, Project, Picture


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    fields = ('name', 'value')

    list_display = ('pk', 'name', 'value')
    list_display_links = ('pk', 'name')

    search_fields = ['name', 'value']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    fields = ('is_visible', 'name')

    list_display = ('pk', 'is_visible', 'name', 'slug')
    list_display_links = ('pk', 'name')

    list_filter = ('is_visible', )
    search_fields = ['name', 'slug']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fields = ('is_visible', 'category', 'name', 'description')

    list_display = ('pk', 'is_visible', 'brand', 'name', 'slug', 'created', 'modified')
    list_display_links = ('pk', 'name')

    list_filter = ('is_visible', 'brand', 'created')
    search_fields = ['name', 'slug', 'description']


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    fields = ('project', 'is_cover', 'is_visible', 'name', 'image', 'position')

    list_display = ('pk', 'project', 'is_cover', 'is_visible', 'name', 'preview', 'position', 'slug', 'created',
                    'modified')
    list_display_links = ('pk', 'name')

    list_filter = ('project', 'is_cover', 'is_visible', 'created')
    search_fields = ['name', 'slug', 'description']
