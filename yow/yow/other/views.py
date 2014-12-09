from pyramid.renderers import render_to_response
from pyramid.view import view_config


def render_result(request, data):
    template = 'yow.other:templates/mytemplate.mak' if False else 'templates/mytemplate.mak'

    return render_to_response(template, data)

@view_config(route_name='root')
def my_view(request):
    return render_result(request, {'project': 'The subproject'})
