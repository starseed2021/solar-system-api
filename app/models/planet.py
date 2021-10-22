from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String) #How to change to name?
    description = db.Column(db.String)
    distance_from_sun_in_km = db.Column(db.Numeric) #How to change datatype?
    moon_count = db.Column(db.Integer)

    def to_string(self):
        return f"{self.id}: {self.name} Description: {self.description}, Distance from the sun: {self.distance_from_sun_in_km}, Moon Count: {self.moon_count}"


