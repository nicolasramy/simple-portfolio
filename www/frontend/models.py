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


class Category(FrontendModel):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return u'{}'.format(self.name)


class Project(FrontendModel):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey('Category')

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
    if sender.__name__ == 'Picture':
        instance.slug = '{}/{}'.format(instance.project.slug, slugify(instance.name))
    elif sender.__name__ == 'Project':
        instance.slug = '{}/{}'.format(instance.category.slug, slugify(instance.name))
    else:
        instance.slug = slugify(instance.name)


pre_save.connect(generate_slug, sender=Category)
pre_save.connect(generate_slug, sender=Project)
pre_save.connect(generate_slug, sender=Picture)
