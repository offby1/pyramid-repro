from pyramid.config import Configurator


def add_home_views(config):
    config.add_route('home', '/')

def add_other_views(config):
    config.add_route('root', '/')


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.include(add_home_views)
    config.include(add_other_views, route_prefix='/other')
    config.scan()
    return config.make_wsgi_app()
