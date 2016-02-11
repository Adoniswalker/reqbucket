import datetime

import short_url
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from main.forms import ContactForm, RequestForm
from main.models import EndPoint, RequestDeport


def contact_view(request):
    form = ContactForm(request.POST or None)
    title = 'Contact Form'
    message = None
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        comment = form.cleaned_data['comment']
        title = 'Thanks!'
        message = 'Thanks for your comment {0}. Will get back to you!'.format(name)
    context = {'form': form, 'title': title, 'message': message}
    template_name = 'main/contact.html'
    return render(request, template_name, context)


@login_required(redirect_field_name="{% url 'account_login' %}")
def get_end_view(request):
    g = EndPoint.objects.filter(whos=request.user)
    message = None
    context = {'g': g, 'message': message}
    template_name = 'main/results.html'
    if len(g) >= 5:
        message = 'Sorry {} you have already reached maximum limits'.format(str(request.user))
        context = {'g': g, 'message': message}
        return render(request, template_name, context)
    else:
        c = EndPoint(whos=request.user)
        c.save()
        return render(request, template_name, context)


class CreateEndPoint(LoginRequiredMixin, generic.CreateView):
    form_class = RequestForm
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        form.instance.whos = self.request.user

        # form.set_cookie('last_connection', datetime.datetime.now())
        # form.set_cookie('username', datetime.datetime.now())
        return super().form_valid(form)


class MainView(View):
    def get(self, request, end_point):
        int_id = short_url.decode_url(end_point)
        id__ = get_object_or_404(EndPoint, pk=int_id)
        request_method = request.META['REQUEST_METHOD']
        # content_length = request.META['CONTENT_LENGTH']
        remote_address = request.META['REMOTE_ADDR']
        http_user_agent = request.META['HTTP_USER_AGENT']
        # body = str(request.body)  # remain
        con_par = str(request.content_type)  # rmafd
        content_params = request.content_params  # go
        if content_params:
            content_params = str(request.content_params)
        else:
            content_params = None
        cookies = request.COOKIES
        if cookies:
            cookies = str(cookies)
        else:
            cookies = None
        # end = EndPoint.objects.get(pk=int_id)
        rd = RequestDeport(end_point=id__, method=request_method, content_type=con_par, content_length=None,
                           remote_address=remote_address,
                           http_user_agent=http_user_agent, body=None, content_params=content_params,
                           COOKIES=cookies)

        rd.save()
        return HttpResponse('ok')

    def post(self, request, end_point):
        int_id = short_url.decode_url(end_point)
        id__ = get_object_or_404(EndPoint, pk=int_id)
        request_method = request.META['REQUEST_METHOD']
        content_length = request.META['CONTENT_LENGTH']
        remote_address = request.META['REMOTE_ADDR']
        http_user_agent = request.META['HTTP_USER_AGENT']
        body = str(request.body)  # remain
        con_par = str(request.content_type)  # rmafd
        content_params = request.content_params  # go
        if content_params: content_params = str(request.content_params)
        else: content_params = None
        cookies = request.COOKIES
        if cookies: cookies = str(cookies)
        else: cookies= None
        # end = EndPoint.objects.get(pk=int_id)
        rd = RequestDeport(end_point=id__, method=request_method, content_type=con_par,content_length = content_length, remote_address= remote_address,
                           http_user_agent=http_user_agent, body=body, content_params=content_params, COOKIES=cookies)

        rd.save()
        return JsonResponse({"results": 0, "result_error": "This is the error"})


