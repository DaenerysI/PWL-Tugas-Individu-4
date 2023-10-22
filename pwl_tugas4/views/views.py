# di views.py

from pyramid.view import view_config
from pyramid.response import Response
from .models import Photo

import json

photos = []

@view_config(route_name='photos', renderer='json', request_method='GET')
def get_photos(request):
    return {'photos': [{'id': photo.id, 'title': photo.title, 'url': photo.url} for photo in photos]}

@view_config(route_name='photos', renderer='json', request_method='POST')
def create_photo(request):
    try:
        data = request.json_body
        photo = Photo(id=len(photos) + 1, title=data['title'], url=data['url'])
        photos.append(photo)
        return {'message': 'Photo Berhasil Dibuat'}
    except Exception as e:
        return {'error': f'Gagal: {str(e)}'}, 400

@view_config(route_name='photo', renderer='json', request_method='GET')
def get_photo(request):
    photo_id = request.matchdict['id']
    photo = next((p for p in photos if p.id == photo_id), None)
    if photo:
        return {'id': photo.id, 'title': photo.title, 'url': photo.url}
    else:
        return {'error': 'Foto tidak ditemukan'}, 404

@view_config(route_name='photo', renderer='json', request_method='PUT')
def update_photo(request):
    try:
        photo_id = request.matchdict['id']
        data = request.json_body
        photo = next((p for p in photos if p.id == photo_id), None)
        if photo:
            photo.title = data['title']
            photo.url = data['url']
            return {'message': 'Photo berhasil terudpate'}
        else:
            return {'error': 'Photo todak ditemukan'}, 404
    except Exception as e:
        return {'error': f'Gagal: {str(e)}'}, 400

@view_config(route_name='photo', renderer='json', request_method='DELETE')
def delete_photo(request):
    photo_id = request.matchdict['id']
    photo = next((p for p in photos if p.id == photo_id), None)
    if photo:
        photos.remove(photo)
        return {'message': 'Photo berhasil dihapus'}
    else:
        return {'error': 'Photo tdak ditemukan'}, 404


@view_config(route_name='register', renderer='json')
def register(request):
    try:
        username = request.json_body.get('username')
        password = request.json_body.get('password')

        if not username or not password:
            return Response(json={'error': 'Gagal identifikasi Username dan password '}, status=400)


        return Response(json={'message': 'Registration successful'}, status=201)
    except json.JSONDecodeError:
        return Response(json={'error': 'Invalid'}, status=400)

@view_config(route_name='login', renderer='json')
def login(request):
    try:
        username = request.json_body.get('username')
        password = request.json_body.get('password')

        if not username or not password:
            return Response(json={'error': 'Gagal identifikasi Username dan Password'}, status=400)


        stored_username = 'user123'
        stored_password = 'password123'  

        if username == stored_username and password == stored_password:
            return Response(json={'message': 'Login successful'}, status=200)
        else:
            return Response(json={'error': 'Invalid '}, status=401)
    except json.JSONDecodeError:
        return Response(json={'error': 'Invalid '}, status=400)

