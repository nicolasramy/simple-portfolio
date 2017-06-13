# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Parameter, Brand, Project, Picture


def contextualize():
    try:
        params = {parameter.name: parameter.value for parameter in Parameter.objects.all()}
    except:
        params = None

    try:
        brands = Brand.objects.filter(is_visible=True)
    except:
        brands = None

    try:
        portrait = Picture.objects.get(is_portrait=True)
    except:
        portrait = None

    return {
        'params': params,
        'brands': brands,
        'portrait': portrait
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


def project_view(request, brand_slug, project_slug):
    context = contextualize()

    current_brand = Brand.objects.filter(is_visible=True).get(slug=brand_slug)
    current_project = Project.objects.filter(is_visible=True).filter(brand_id=current_brand.id).get(slug=project_slug)

    context['current_brand'] = current_brand
    context['current_project'] = current_project

    return render(request, 'default/pages/project.html', context)
