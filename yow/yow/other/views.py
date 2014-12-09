from pyramid.view import view_config


@view_config(route_name='root', renderer='json')
def my_view(request):
    return "Hi, I'm the root view"
