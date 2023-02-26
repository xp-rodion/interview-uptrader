from django.views.generic import TemplateView
from treemenu.view_mixin import MixinView


class MenuView(MixinView, TemplateView):
    template_name = 'index.html'
    title = 'Head page'


class ItemMenuView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, req_item, **kwargs):
        context = super(ItemMenuView, self).get_context_data(**kwargs)
        context['req_item'] = req_item
        return context
