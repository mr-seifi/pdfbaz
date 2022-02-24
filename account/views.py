from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


class Dashboard(TemplateView):
    template_name = 'account/dashboard.html'
    extra_context = {'section': 'dashboard'}

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(Dashboard, self).dispatch(request, *args, **kwargs)