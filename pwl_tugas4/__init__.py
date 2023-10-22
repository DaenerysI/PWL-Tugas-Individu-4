from pyramid.config import Configurator
from .views import get_photos, create_photo, get_photo, update_photo, delete_photo
def main(global_config, **settings):
    config = Configurator(settings=settings)

    config.add_route('register', '/register')
    config.add_route('login', '/login')
    config.include('.views')
    config.add_route('photos', '/photos')
    config.add_view(get_photos, route_name='photos', renderer='json')
    config.add_view(create_photo, route_name='photos', renderer='json', request_method='POST')
    config.add_route('photo', '/photos/{id}')
    config.add_view(get_photo, route_name='photo', renderer='json', request_method='GET')
    config.add_view(update_photo, route_name='photo', renderer='json', request_method='PUT')
    config.add_view(delete_photo, route_name='photo', renderer='json', request_method='DELETE')
    
    return config.make_wsgi_app()
