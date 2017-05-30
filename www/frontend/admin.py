# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Parameter, Category, Project, Picture


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    fields = ('name', 'value')

    list_display = ('pk', 'name', 'value')
    list_display_links = ('pk', 'name')

    search_fields = ['name', 'value']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('is_active', 'name')

    list_display = ('pk', 'is_active', 'name', 'slug')
    list_display_links = ('pk', 'name')

    list_filter = ('is_active', )
    search_fields = ['name', 'slug']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fields = ('is_published', 'category', 'name', 'description')

    list_display = ('pk', 'is_published', 'category', 'name', 'slug', 'created', 'modified')
    list_display_links = ('pk', 'name')

    list_filter = ('is_published', 'category', 'created')
    search_fields = ['name', 'slug', 'description']


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    fields = ('project', 'is_cover', 'name', 'image', 'position')

    list_display = ('pk', 'project', 'is_cover', 'name', 'preview', 'position', 'slug', 'created', 'modified')
    list_display_links = ('pk', 'name')

    list_filter = ('project', 'is_cover', 'created')
    search_fields = ['name', 'slug', 'description']
