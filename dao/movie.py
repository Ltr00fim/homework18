from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, id):
        return self.session.query(Movie).get(id)

    def create(self, data):
        new = Movie(**data)
        self.session.add(new)
        self.session.commit()
        return new

    def get_all(self):
        return self.session.query(Movie).all()

    def delete(self, id):
        self.session.delete(self.get_one(id))

    def update(self, data, id):
        update = self.get_one(id)
        update.title = data.get('title')
        update.description = data.get('description')
        update.trailer = data.get('trailer')
        update.year = data.get('year')
        update.rating = data.get('rating')
        update.genre_id = data.get('genre_id')
        update.genre = data.get('genre')
        update.director_id = data.get('director_id')
        update.director = data.get('director')
        self.session.add(update)
        self.session.commit()
