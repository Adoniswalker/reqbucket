from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import generic
from main.models import RequestDeport, EndPoint
import short_url

domain = 'http://127.0.0.1:8000'


def url_data(request, end_id):
    data =  RequestDeport.objects.filter(end_point = end_id)
    seriali = serializers.serialize('json', data)
    # valus_list = list(data.values())
    # valus_list = {'query_set':seriali}
    return HttpResponse(seriali)


class DashBoard(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'accounts/dash_board.html'
    select_related = ('endpoints',)

    def get_object(self, queryset=None):
        return self.request.user


# class DashBoardView(LoginRequiredMixin, generic.DetailView):
#     model = User
#     template_name = 'accounts/dash_board.html'
#     select_related = ('endpoints', 'request_data')
#
#     # def get_object(self, queryset=None):
#     #     print(self.kwargs.get('request_end', None))
#     #     print('hash')
#     #     return self.request.user
#
#     def get_context_data(self, **kwargs):
#         context = super(DashBoardView, self).get_context_data(**kwargs)
#         context['keyends'] = RequestDeport.objects.filter(
#             end_point=short_url.decode_url(self.kwargs.get('request_end')))
#         return context
#         #     return queryset.get(end_point = short_url.decode_url(self.kwargs.get('request_end', None)))
#

class DashboardFuc(generic.ListView):
    template_name = 'main/results.html'
    context_object_name = 'request_url'

    def get_queryset(self):
        end_point = short_url.decode_url(self.kwargs.get('end_point'))
        print(end_point)
        return RequestDeport.objects.filter(end_point=end_point)

        # def get_context_data(self, **kwargs):
        #     # Call the base implementation first to get a context
        #     context = super(DashboardFuc, self).get_context_data(**kwargs)
        #     # Add in a QuerySet of all the books
        #     context['book_list'] = RequestDeport.objects.all()
        #     return context
        # def get_context_data(self, **kwargs):
        #     # Call the base implementation first to get a context
        #     context = super(DashboardFuc, self).get_context_data(**kwargs)
        #     # Add in a QuerySet of all the books
        #     context['book_list'] = RequestDeport.objects.all()
        #     return context
