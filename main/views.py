from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView

from main.forms import ContactForm
from main.models import EndPoint


def contact_view(request):
    form = ContactForm(request.POST or None)
    title = 'Contact Form'
    message = None
    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        comment = form.cleaned_data['comment']
        title= 'Thanks!'
        message = 'Thanks for your comment {0}. Will get back to you!'.format(name)
    context = {'form':form, 'title':title, 'message':message}
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

class MainView(View):
    def get(self, request, id):
        id__ = get_object_or_404(EndPoint, pk=id)
        head = request.scheme#remain
        body = request.body#go
        path = request.path_info#remain
        content_params = request.content_params#go
        con_par = request.content_type#remain
        encoding = request.encoding
        COOKIES = request.COOKIES
        FILES = request.FILES
        META = request.META
        return HttpResponse(META)


    def post(self, request):
        id__ = get_object_or_404(EndPoint, whos=id)
        head = request.scheme#remain
        body = str(request.body)#remain
        path = str(request.path_info)#remain
        content_params = str(request.content_params)#go
        con_par = str(request.content_type)#rma
        encoding = str(request.encoding)
        COOKIES = str(request.COOKIES)
        FILES = str(request.FILES)
        META = request.META
        return JsonResponse({"resut":0,"resulterro":META})