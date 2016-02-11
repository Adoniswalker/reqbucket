from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import  generic

domain = 'http://127.0.0.1:8000'


class DashBoard(LoginRequiredMixin, generic.DetailView ):
    model = User
    template_name = 'accounts/dash_board.html'
    select_related = ('endpoints',)

    def get_object(self, queryset = None):
        return self.request.user