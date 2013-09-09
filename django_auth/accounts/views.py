# coding: utf-8
#from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
#from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator

from accounts.forms import RegisterForm


class RegisterView(CreateView):
    model = User
    template_name = "accounts/register.html"
    form_class = RegisterForm

    #用success_url出现函数参数提前调用的情况
    #success_url = reverse('profile')
    def get_success_url(self):
        return reverse('login')
