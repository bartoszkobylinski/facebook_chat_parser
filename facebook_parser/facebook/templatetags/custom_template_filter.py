from django import template

register = template.Library()


@register.filter
def divideby(value, arg):
    if int(arg) != 0:
        return round(int(value)/int(arg), 2)
    else:
        return 0


register.filter('divideby', divideby)
