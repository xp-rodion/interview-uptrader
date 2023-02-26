from django import template
from treemenu.models import Menu

register = template.Library()


@register.inclusion_tag('tags/menu.html')
def draw_menu(slug, req_item=None):
    menu = Menu.objects.prefetch_related('item_menu').get(slug=slug)
    return {'menu': menu, 'req_item': req_item}
