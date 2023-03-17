from flask_restx import Resource, Namespace
from implemented import *
from dao.model.director import DirectorSchema
from flask import request

director_ns = Namespace('director')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        data = movie_service.get_all()
        return DirectorSchema(many=True).dump(data), 200

    def post(self):
        data = movie_service.create(request.json)
        return DirectorSchema(many=False).dump(data), 201


@director_ns.route('/<id>')
class DirectorView(Resource):
    def get(self, id):
        data = movie_service.get_one(int(id))
        return DirectorSchema().dump(data), 200

    def delete(self, id):
        movie_service.delete(int(id))
        return "", 204

    def update(self, id):
        movie_service.update(int(id), request.json)
        return "", 200
