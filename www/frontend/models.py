# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings

from adminsortable.models import SortableMixin


def get_upload_to_path(instance, filename):
    if not instance.project:
        return filename
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


class Brand(FrontendModel, SortableMixin):
    is_visible = models.BooleanField(default=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    brand_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['brand_order']
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

    def __unicode__(self):
        return u'{}'.format(self.name)

    def projects(self):
        return Project.objects.filter(brand_id=self.id).filter(is_visible=True).all()


class Project(FrontendModel, SortableMixin):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    is_visible = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    brand = models.ForeignKey('Brand')
    are_pictures_inline = models.BooleanField(default=False)

    project_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    class Meta:
        ordering = ['project_order']
        verbose_name = 'project'
        verbose_name_plural = 'projects'

    def __unicode__(self):
        return u'{} / {}'.format(self.brand, self.name)


class Picture(FrontendModel, SortableMixin):
    name = models.CharField(max_length=200, blank=True)
    header = models.CharField(max_length=200, blank=True)
    slug = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    is_visible = models.BooleanField(default=False)
    is_fluid = models.BooleanField(default=False)

    project = models.ForeignKey('Project', blank=True, null=True)
    image = models.ImageField(upload_to=get_upload_to_path)

    picture_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def preview(self):
        if self.image:
            return u'<img src="{}{}" title="{}" weight="200" height="80">'.format(settings.MEDIA_URL,
                                                                                  self.image,
                                                                                  self.name)
        else:
            return None

    def absolute_url(self):
        if self.image:
            return u'{}{}{}'.format(settings.SITE_URL, settings.MEDIA_URL, self.image)
        else:
            return False

    def has_header(self):
        return bool(len(self.header))

    preview.short_description = 'Image'
    preview.allow_tags = True

    class Meta:
        ordering = ['picture_order']
        verbose_name = 'picture'
        verbose_name_plural = 'pictures'

    def __unicode__(self):
        return u'{}'.format(self.name)


class Document(FrontendModel):
    name = models.CharField(max_length=200, blank=True)
    slug = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    is_visible = models.BooleanField(default=False)

    project = models.ForeignKey('Project', blank=True, null=True)
    document = models.FileField(upload_to=get_upload_to_path)

    class Meta:
        ordering = ['-created']
        verbose_name = 'document'
        verbose_name_plural = 'documents'

    def __unicode__(self):
        return u'{}'.format(self.name)

    def absolute_url(self):
        if self.document:
            return u'{}{}{}'.format(settings.SITE_URL, settings.MEDIA_URL, self.document)
        else:
            return False


class Video(FrontendModel):
    name = models.CharField(max_length=200, blank=True)
    slug = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    is_visible = models.BooleanField(default=False)

    project = models.ForeignKey('Project', blank=True, null=True)
    video = models.FileField(upload_to=get_upload_to_path)

    class Meta:
        ordering = ['-created']
        verbose_name = 'video'
        verbose_name_plural = 'videos'

    def __unicode__(self):
        return u'{}'.format(self.name)

    def absolute_url(self):
        if self.video:
            return u'{}{}{}'.format(settings.SITE_URL, settings.MEDIA_URL, self.video)
        else:
            return False


def generate_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.name)


def auto_fill_name(sender, instance, **kwargs):
    if not len(instance.name):
        if sender.__name__ == 'Picture':
            instance.name = instance.image

        elif sender.__name__ == 'Document':
            instance.name = instance.document

        elif sender.__name__ == 'Video':
            instance.name = instance.video


def generate_parameter_name(sender, instance, **kwargs):
    instance.name = slugify(instance.name).replace('-', '_')


pre_save.connect(generate_slug, sender=Brand)
pre_save.connect(generate_slug, sender=Project)
pre_save.connect(generate_slug, sender=Picture)
pre_save.connect(generate_slug, sender=Document)

pre_save.connect(auto_fill_name, sender=Picture)
pre_save.connect(auto_fill_name, sender=Document)
pre_save.connect(auto_fill_name, sender=Video)

pre_save.connect(generate_parameter_name, sender=Parameter)
