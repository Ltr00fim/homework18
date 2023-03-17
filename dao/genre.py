from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, id):
        return self.session.query(Genre).get(id)

    def create(self, data):
        new = Genre(**data)
        self.session.add(new)
        self.session.commit()
        return new

    def get_all(self):
        return self.session.query(Genre).all()

    def delete(self, id):
        self.session.delete(self.get_one(id))

    def update(self, data, id):
        update = self.get_one(id)
        update.name = data.get('name')
        self.session.add(update)
        self.session.commit()
