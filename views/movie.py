from flask_restx import Resource, Namespace
from implemented import *
from dao.model.movie import MovieSchema
from flask import request

movie_ns = Namespace('movie')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        data = movie_service.get_all()
        return MovieSchema(many=True).dump(data), 200

    def post(self):
        data = movie_service.create(request.json)
        return MovieSchema(many=False).dump(data), 201


@movie_ns.route('/<id>')
class MovieView(Resource):
    def get(self, id):
        data = movie_service.get_one(int(id))
        return MovieSchema().dump(data), 200

    def delete(self, id):
        movie_service.delete(int(id))
        return "", 204

    def update(self, id):
        movie_service.update(int(id), request.json)
        return "", 200
