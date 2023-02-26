from django import template

from treemenu.models import ItemMenu

register = template.Library()


@register.inclusion_tag('tags/item_menu.html')
def draw_item_menu(req_item):
    list_parents = []
    manager = ItemMenu.objects
    try:
        """Catch errors due to parent"""
        req_item = manager.get(parent__slug=req_item)
    except ItemMenu.DoesNotExist:
        req_item = manager.get(slug=req_item)
    while True:
        list_parents.append(req_item)
        print(req_item)
        if req_item.menu:
            break
        req_item = req_item.parent
    return {'item_menu': list_parents[::-1]}