# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Parameter, Category, Project, Picture


def contextualize():
    return {
        'params': {parameter.name: parameter.value for parameter in Parameter.objects.all()},
        'projects': Project.objects.filter(is_published=True)
    }


def index(request):
    context = contextualize()
    return render(request, 'default/pages/index.html', context)


def category_index(request):
    context = contextualize()

    categories = Category.objects.filter(is_active=True)
    context['categories'] = categories

    return render(request, 'default/pages/categories.html', context)


def category_view(request):
    context = contextualize()

    return render(request, 'default/pages/category.html', context)


def project_index(request):
    context = contextualize()

    return render(request, 'default/pages/projects.html', context)


def project_view(request, project_slug):
    context = contextualize()

    current_project = Project.objects.filter(is_published=True).get(slug=project_slug)
    context['current_project'] = current_project

    return render(request, 'default/pages/project.html', context)
