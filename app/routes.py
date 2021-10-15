from flask import Blueprint, jsonify

class Planets:
    def __init__(self, id, name, description, distance_from_sun_in_km):
        self.id = id
        self.name = name
        self.description = description
        self.distance_from_sun = distance_from_sun_in_km

planets = [
    Planets(1, "Earth", "Our home planet; inner rocky planet", "149,600,000 km"),
    Planets(2, "Mercury", "The smallest and fastest planet; inner rocky planet.", "57,900,000 km"),
    Planets(3, "Venus", "The hottest planet in our solar system.", "108,200,000 km"),
    Planets(4, "Mars", "A dusty, cold, desert world with a thin atmosphere.", "227,900,000 km"),
    Planets(5, "Jupiter", "The largest planet in our solar system.", "778,600,000 km"),
    Planets(6, "Saturn", "Adorned with icy rings; gas planet.", "1,433,500,000 km"),
    Planets(7, "Uranus", "Seventh planet from the sun; rotates at nearly 90° degrees.", "2,872,500,000 km"),
    Planets(8, "Neptune", "The most distant planet; dark, cold, and with supersonic winds.", "4,495,100,000 km")
]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["GET"])
def planet_facts():
    pass