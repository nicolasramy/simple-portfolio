# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'default/pages/index.html', context)


def categories(request):
    context = {}
    return render(request, 'default/pages/categories.html', context)


def category(request):
    context = {}
    return render(request, 'default/pages/category.html', context)


def projects(request):
    context = {}
    return render(request, 'default/pages/projects.html', context)


def project(request):
    context = {}
    return render(request, 'default/pages/project.html', context)
