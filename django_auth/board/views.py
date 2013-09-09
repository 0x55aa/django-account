# coding: utf-8
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from board.models import Board
from board.forms import AddMessageForm


class BoardListView(ListView):
    model = Board
    paginate_by = '10'
    context_object_name = 'boards'


class AddMessageView(CreateView):
    model = Board
    template_name = "board/add_message.html"
    form_class = AddMessageForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AddMessageView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('message_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.ip = self.request.META['REMOTE_ADDR']
        return super(AddMessageView, self).form_valid(form)
