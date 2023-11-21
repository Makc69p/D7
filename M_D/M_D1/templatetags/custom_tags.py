from django.contrib.auth.decorators import login_required

@login_required
def show_protected_page(request):


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
   d = context['request'].GET.copy()
   for k, v in kwargs.items():
       d[k] = v
   return d.urlencode()