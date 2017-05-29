# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class FrontendModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Project(FrontendModel):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'

    def __unicode__(self):
        return u'{}'.format(self.name)


class Picture(FrontendModel):
    title = models.CharField(max_length=200, blank=True)
    slug = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio')
    position = models.IntegerField(blank=True, null=True)
    is_cover = models.BooleanField(default=False)

    project = models.ForeignKey('Project')

    class Meta:
        verbose_name = 'picture'
        verbose_name_plural = 'pictures'

    def __unicode__(self):
        return u'{}'.format(self.title)
