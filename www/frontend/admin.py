# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Category, Project, Picture


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

    list_filter = ('is_published', 'category')
    search_fields = ['name', 'slug', 'description']


admin.site.register(Picture)
