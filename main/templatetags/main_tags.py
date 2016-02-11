from django import template

from ..forms import RequestForm

register = template.Library()


@register.inclusion_tag('main/_url_tag.html')
def url_tag():
    form = RequestForm()
    return {'form': form}
