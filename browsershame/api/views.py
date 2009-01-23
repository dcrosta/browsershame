import simplejson 

from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.http import HttpResponse

from browsershame.api.models import Browser
from browsershame.api.models import Sample

def _to_int(*args):
    for arg in args:
        try:
            yield int(arg)
        except:
            yield None

def _get_field_names(model):
    return [f.name for f in model._meta._fields() if not f.primary_key]

def _model_as_json(model, fields=None):
    if fields is None:
        fields = _get_field_names(model)
    d = {}
    for field in fields:
        d[field] = getattr(model, field)
    return simplejson.dumps(d)

def _model_list_as_json(model_list, fields=None):
    if len(model_list) == 0:
        return '[]' # empty list
    if fields is None:
        # assume the list is all of the same
        # type of model -- seems fair for now
        fields = _get_field_names(model_list[0])
    l = []
    for model in model_list:
        d = {}
        for field in fields:
            d[field] = getattr(model, field)
        l.append(d)
    return simplejson.dumps(l)

def get_browser(request, name, major, minor, tick):
    major, minor, tick = _to_int(major, minor, tick)
    browser = get_object_or_404(
            Browser,
            name=name,
            major=major,
            minor=minor,
            tick=tick)
    json = _model_as_json(browser)
    return HttpResponse(json)

def list_browsers(request, name, major, minor, tick):
    major, minor, tick = _to_int(major, minor, tick)
    kwargs = {}
    for key in ('major', 'minor', 'tick'):
        val = locals()[key]
        if val is not None:
            kwargs[key] = val
    browsers = get_list_or_404(Browser, name=name, **kwargs)
    print browsers
    json = _model_list_as_json(browsers)
    return HttpResponse(json)
