from django import template

register = template.Library()


@register.simple_tag
def lower(letter):
    return letter.lower()