from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

from allauth.account.forms import SignupForm


class ProductSearchForm(forms.Form):
    query = forms.CharField(label='Поиск', max_length=100)


class LocalSignupForm(SignupForm):
    def try_save(self, request):
        print('----------- try_save ------------')
        if self.account_already_exists:
            user = None
            resp = HttpResponseRedirect(reverse('account_email_conflict'))
        else:
            user = self.save(request)
            resp = None
        return user, resp
