# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings


def get_upload_to_path(instance, filename):
    return os.path.join(instance.project.slug, filename)


class FrontendModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Parameter(FrontendModel):
    name = models.CharField(max_length=200)
    value = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'parameter'
        verbose_name_plural = 'parameters'

    def __unicode__(self):
        return u'{}'.format(self.name)


class Brand(FrontendModel):
    is_visible = models.BooleanField(default=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

    def __unicode__(self):
        return u'{}'.format(self.name)


class Project(FrontendModel):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    is_visible = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    brand = models.ForeignKey('Brand')

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'

    def __unicode__(self):
        return u'{}'.format(self.name)


class Picture(FrontendModel):
    name = models.CharField(max_length=200, blank=True)
    slug = models.CharField(max_length=200)
    position = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_cover = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=False)

    project = models.ForeignKey('Project')
    image = models.ImageField(upload_to=get_upload_to_path)

    def preview(self):
        if self.image:
            return u'<img src="{}{}" title="{}" weight="200" height="80">'.format(settings.MEDIA_URL,
                                                                                  self.image,
                                                                                  self.name)
        else:
            return None

    preview.short_description = 'Image'
    preview.allow_tags = True

    class Meta:
        verbose_name = 'picture'
        verbose_name_plural = 'pictures'

    def __unicode__(self):
        return u'{}'.format(self.name)


def generate_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.name)


def generate_parameter_name(sender, instance, **kwargs):
    instance.name = slugify(instance.name).replace('-', '_')


pre_save.connect(generate_slug, sender=Brand)
pre_save.connect(generate_slug, sender=Project)
pre_save.connect(generate_slug, sender=Picture)

pre_save.connect(generate_parameter_name, sender=Parameter)
