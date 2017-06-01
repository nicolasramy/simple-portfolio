# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db import models

from adminsortable.admin import SortableAdmin
from pagedown.widgets import AdminPagedownWidget

from .models import Parameter, Brand, Project, Picture


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    fields = ('name', 'value')

    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

    list_display = ('pk', 'name', 'value')
    list_display_links = ('pk', 'name')

    search_fields = ['name', 'value']


@admin.register(Brand)
class BrandAdmin(SortableAdmin):
    fields = ('is_visible', 'name', 'description')

    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

    list_display = ('pk', 'is_visible', 'name', 'slug')
    list_display_links = ('pk', 'name')

    list_filter = ('is_visible', )
    search_fields = ['name', 'slug']


@admin.register(Project)
class ProjectAdmin(SortableAdmin):
    fields = ('is_visible', 'brand', 'name', 'description')

    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

    list_display = ('pk', 'is_visible', 'brand', 'name', 'slug', 'created', 'modified')
    list_display_links = ('pk', 'name')

    list_filter = ('is_visible', 'brand', 'created')
    search_fields = ['name', 'slug', 'description']


@admin.register(Picture)
class PictureAdmin(SortableAdmin):
    fields = ('project', 'is_portrait', 'is_cover', 'is_visible', 'name', 'image', 'description')

    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

    list_display = ('pk', 'project', 'is_portrait', 'is_cover', 'is_visible', 'name', 'preview', 'slug',
                    'created', 'modified')
    list_display_links = ('pk', 'name')

    list_filter = ('project', 'is_portrait', 'is_cover', 'is_visible', 'created')
    search_fields = ['name', 'slug', 'description']
