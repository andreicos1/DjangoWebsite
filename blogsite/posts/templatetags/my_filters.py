from django import template
register = template.Library()

@register.filter
def pyrange(number):
    return range(number)

@register.filter(name='incthree')
def incthree(number):
    return range(0, number, 3)

@register.filter
def get_at_index(the_list, index):
    return the_list[index]
