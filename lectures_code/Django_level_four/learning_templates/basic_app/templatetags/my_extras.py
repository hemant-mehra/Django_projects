from django import template

register = template.Library()

def cut(value,arg):
    """
    this cuts out all value of 'árg' strings!

    """
    return value.replace(arg,'')

register.filter('cut',cut)
