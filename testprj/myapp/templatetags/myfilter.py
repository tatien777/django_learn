from django.template import Library

register = Library()

@register.filter
def make_range(num):
    return range(1,num+1)