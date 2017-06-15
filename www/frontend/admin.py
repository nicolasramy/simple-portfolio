# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db import models

from adminsortable.admin import SortableAdmin, NonSortableParentAdmin, SortableStackedInline
from pagedown.widgets import AdminPagedownWidget

from .models import Parameter, Brand, Project, Picture, Document, Video


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    fields = ('name', 'value')

    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }

    list_display = ('pk', 'name', 'value')
    list_display_links = ('pk', 'name')

    search_fields = ['name', 'value']


@admin.register(Brand)
class BrandAdmin(SortableAdmin):
    fields = ('is_visible', 'name', 'description')

    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }

    list_display = ('pk', 'is_visible', 'name', 'slug')
    list_display_links = ('pk', 'name')

    list_filter = ('is_visible', )
    search_fields = ['name', 'slug']


@admin.register(Picture)
class PictureAdmin(SortableAdmin):
    fields = ('project', 'is_visible', 'is_fluid', 'header', 'name', 'image', 'description')

    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }

    list_display = ('pk', 'project', 'is_visible', 'is_fluid', 'header', 'name', 'preview', 'absolute_url', 'slug')
    list_display_links = ('pk', 'name')

    list_filter = ('project', 'is_visible', 'is_fluid', 'created')
    search_fields = ['header', 'name', 'slug', 'description']


@admin.register(Document)
class DocumentAdmin(SortableAdmin):
    fields = ('project', 'is_visible', 'name', 'document', 'description')

    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }

    list_display = ('pk', 'project', 'is_visible', 'name', 'slug', 'created', 'modified')
    list_display_links = ('pk', 'name')

    list_filter = ('project', 'is_visible', 'created')
    search_fields = ['name', 'slug', 'description']


@admin.register(Video)
class VideoAdmin(SortableAdmin):
    fields = ('project', 'is_visible', 'name', 'video', 'description')

    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }

    list_display = ('pk', 'project', 'is_visible', 'name', 'slug', 'created', 'modified')
    list_display_links = ('pk', 'name')

    list_filter = ('project', 'is_visible', 'created')
    search_fields = ['name', 'slug', 'description']


class PictureInline(SortableStackedInline):
    model = Picture
    extra = 1

    fields = ('is_visible', 'is_fluid', 'header', 'name', 'image')


@admin.register(Project)
class ProjectAdmin(SortableAdmin):
    fields = ('is_visible', 'are_pictures_inline', 'brand', 'name', 'description')
    inlines = [PictureInline]

    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }

    list_display = ('pk', 'is_visible', 'brand', 'name', 'slug', 'created', 'modified')
    list_display_links = ('pk', 'name')

    list_filter = ('is_visible', 'are_pictures_inline', 'brand', 'created')
    search_fields = ['name', 'slug', 'description']
