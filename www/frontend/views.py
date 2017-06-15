# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Parameter, Brand, Project, Picture, Document, Video


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
    current_pictures = Picture.objects.filter(is_visible=True).filter(project_id=current_project.id).all()
    current_videos = Video.objects.filter(is_visible=True).filter(project_id=current_project.id).all()
    current_documents = Document.objects.filter(is_visible=True).filter(project_id=current_project.id).all()

    context['current_brand'] = current_brand
    context['current_project'] = current_project

    if len(current_pictures):
        context['current_pictures'] = {}
        result_group = 0
        for position, picture in enumerate(current_pictures):
            if position == 0 or picture.has_header():
                result_group += 1
                context['current_pictures'][result_group] = {
                    'header': picture.header,
                    'pictures': []
                }

            context['current_pictures'][result_group]['pictures'].append(picture)

    if len(current_videos):
        context['current_videos'] = {}
        result_group = 0
        for position, video in enumerate(current_videos):
            if position == 0 or video.has_header():
                result_group += 1
                context['current_videos'][result_group] = {
                    'header': video.header,
                    'videos': []
                }

            context['current_videos'][result_group]['videos'].append(video)

    if len(current_documents):
        context['current_documents'] = {}
        result_group = 0
        for position, document in enumerate(current_documents):
            if position == 0 or document.has_header():
                result_group += 1
                context['current_documents'][result_group] = {
                    'header': document.header,
                    'documents': []
                }

            context['current_documents'][result_group]['documents'].append(document)

    return render(request, 'default/pages/project.html', context)
