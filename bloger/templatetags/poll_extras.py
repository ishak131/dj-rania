from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)[1]

def get_lang(value, key):
    return value.split(key)[1]

register.filter('split', split)
register.filter('get_lang', get_lang)