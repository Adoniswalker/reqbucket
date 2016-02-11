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
        return super().form_valid(form)


class MainView(View):
    def get(self, request, end_point):
        int_id = short_url.decode_url(end_point)
        id__ = get_object_or_404(EndPoint, pk=int_id)
        head = request.scheme  # remain
        body = request.body  # go
        path = str(request.path_info)  # remain
        content_params = request.content_params  # go
        con_par = request.content_type  # remain
        encoding = request.encoding
        cookies = request.COOKIES
        FILES = request.FILES
        META = request.META
        end = EndPoint.objects.get(pk=int_id)
        rd = RequestDeport(end_point=end, content_type=con_par, body=body, content_params=content_params,
                           encoding=str(encoding), COOKIES=str(cookies), meta_header=str(META))
        # print(head,path,FILES)
        rd.save()
        return HttpResponse('ok')

    def post(self, request, end_point):
        int_id = short_url.decode_url(end_point)
        id__ = get_object_or_404(EndPoint, pk=int_id)
        head = request.scheme  # remain
        body = str(request.body)  # remain
        path = str(request.path_info)  # remain
        content_params = str(request.content_params)  # go
        con_par = str(request.content_type)  # rmafd
        encoding = str(request.encoding)
        cookies = str(request.COOKIES)
        FILES = str(request.FILES)
        META = request.META
        # print(head,path,FILES)
        end = EndPoint.objects.get(pk=int_id)
        rd = RequestDeport(end_point=end, content_type=con_par, body=body, content_params=content_params,
                           encoding=str(encoding), COOKIES=str(cookies), meta_header=str(META))

        rd.save()
        return JsonResponse({"resut": 0, "resulterro": "This is the error"})
