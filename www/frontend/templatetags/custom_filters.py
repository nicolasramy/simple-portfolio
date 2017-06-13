from django import template

import markdown


register = template.Library()


@register.filter
def markdownify(value):
    return markdown.markdown(value, extensions=['extra', 'attr_list', 'def_list', 'nl2br', 'toc'])


@register.filter
def modulo(value, divider):
    return value % divider


@register.filter
def get_dict(data, value):
    try:
        result = data[value]
    except KeyError:
        result = None

    return result


@register.filter
def to_text(value):
    if value == 1:
        return 'one'
    elif value == 2:
        return 'two'
    else:
        return 'three'
