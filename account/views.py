from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from .forms import UserRegistrationForm


class Register(TemplateView):
    template_name = 'account/register.html'
    extra_context = {'user_form': UserRegistrationForm()}

    def post(self, request, *args, **kwargs):
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})


class Dashboard(TemplateView):
    template_name = 'account/dashboard.html'
    extra_context = {'section': 'dashboard'}

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(Dashboard, self).dispatch(request, *args, **kwargs)
