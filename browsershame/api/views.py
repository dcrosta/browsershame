from django.shortcuts import get_object_or_404

from browsershame.api.models import Browser
from browsershame.api.models import Sample

def _model_as_json(model):
    print model._meta.get_all_field_names()

def get_browser(request, name, major, minor, tick):
    kwargs = {}
    for var in ('name', 'major', 'minor', 'tick'):
        if locals()[var] != None:
            kwargs[var] = locals()[var]
    browser = get_object_or_404(Browser, **kwargs)
    _model_as_json(browser)
    return HttpResponse('hi')
