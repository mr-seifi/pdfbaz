from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.generic import TemplateView

from .forms import LoginForm


class UserLogin(TemplateView):
    template_name = 'account/login.html'
    extra_context = {'form': LoginForm()}

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
        UserLogin.extra_context['form'] = form
