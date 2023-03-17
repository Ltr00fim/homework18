from flask_restx import Resource, Namespace
from implemented import *
from dao.model.genre import GenreSchema
from flask import request

genre_ns = Namespace('genre')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        data = movie_service.get_all()
        return GenreSchema(many=True).dump(data), 200

    def post(self):
        data = movie_service.create(request.json)
        return GenreSchema(many=False).dump(data), 201


@genre_ns.route('/<id>')
class GenreView(Resource):
    def get(self, id):
        data = movie_service.get_one(int(id))
        return GenreSchema().dump(data), 200

    def delete(self, id):
        movie_service.delete(int(id))
        return "", 204

    def update(self, id):
        movie_service.update(int(id), request.json)
        return "", 200
