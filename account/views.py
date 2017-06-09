from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse

from account.forms import RegistrationForm


def account_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.user_cache)
            return HttpResponseRedirect(reverse('show_all_tasks'))
        else:
            return TemplateResponse(request, 'login.html', {'error': True})
    else:
        return TemplateResponse(request, 'login.html', {})


@login_required
def account_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def account_register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data.get('username')
            )
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return HttpResponseRedirect(reverse('show_all_tasks'))
        return TemplateResponse(request, 'register.html', {'errors': form.errors})
    else:
        return TemplateResponse(request, 'register.html', {})
