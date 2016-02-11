from django import template

from main.models import RequestDeport
from ..forms import RequestForm

register = template.Library()


@register.inclusion_tag('main/_url_tag.html')
def url_tag():
    form = RequestForm()
    return {'form': form}


# @register.inclusion_tag('accounts/dash_board.html')
@register.filter
def no_requests(value):
    return RequestDeport.objects.filter(end_point__id=value).count()
