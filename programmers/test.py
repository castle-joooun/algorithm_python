class Database:
    db = {}

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def insert(self, field, value):
        if len(self.db) < self.size:
            self.db[field] = value

    def select(self, field):
        return self.db[field]

    def update(self, field, value):
        self.db[field] = value

    def delete(self, field):
        del self.db[field]


db = Database("mysql", 3)
db.insert("name", "정우성")
db.insert("age", 35)
db.insert("height", 185)

print(db.select("name"))
db.delete("name")