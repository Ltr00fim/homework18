class MovieService:
    def __init__(self, dao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, id):
        return self.dao.get_one(id)

    def create(self, data):
        return self.dao.create(data)

    def delete(self, id):
        return self.dao.delete(id)

    def update(self, id, data):
        return self.dao.update(id, data)
