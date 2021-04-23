from django.template import Library

register = Library()


@register.filter()
def replace_comma_to_dot(value):
    return str(value).replace(',','.') if value else None
