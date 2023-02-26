from django.views.generic import TemplateView


class MixinView(TemplateView):
    title = None

    def get_context_data(self, **kwargs):
        context = super(MixinView, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context

