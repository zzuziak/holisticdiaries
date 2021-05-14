from django import template

register = template.Library()

@register.simple_tag
def cat_menu(request):
    return Category.objects.all()
