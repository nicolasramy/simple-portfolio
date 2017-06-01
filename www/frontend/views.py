# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Parameter, Brand, Project, Picture


def contextualize():
    return {
        'params': {parameter.name: parameter.value for parameter in Parameter.objects.all()},
        'brands': Brand.objects.filter(is_visible=True)
    }


def index(request):
    context = contextualize()
    return render(request, 'default/pages/index.html', context)


def brand_index(request):
    context = contextualize()

    brands = Brand.objects.filter(is_visible=True)
    context['brands'] = brands

    return render(request, 'default/pages/brands.html', context)


def brand_view(request, brand_slug):
    context = contextualize()

    current_brand = Brand.objects.filter(is_visible=True).get(slug=brand_slug)
    context['current_brand'] = current_brand

    return render(request, 'default/pages/brand.html', context)


def project_index(request):
    context = contextualize()

    return render(request, 'default/pages/projects.html', context)


def project_view(request, project_slug):
    context = contextualize()

    current_project = Project.objects.filter(is_visible=True).get(slug=project_slug)
    context['current_project'] = current_project

    return render(request, 'default/pages/project.html', context)
