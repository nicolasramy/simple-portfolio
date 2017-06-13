from django import template

import markdown


register = template.Library()


@register.filter
def markdownify(value):
    return markdown.markdown(value, extensions=['extra', 'attr_list', 'def_list', 'nl2br', 'toc'])


@register.filter
def modulo(value, divider):
    return value % divider
