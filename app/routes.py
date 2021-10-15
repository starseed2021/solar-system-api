from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, distance_from_sun_in_km):
        self.id = id
        self.name = name
        self.description = description
        self.distance_from_sun_in_km = distance_from_sun_in_km

planets = [
    Planet(1, "Mercury", "The smallest and fastest planet; inner rocky planet.", "57,900,000 km"),
    Planet(2, "Venus", "The hottest planet in our solar system.", "108,200,000 km"),
    Planet(3, "Earth", "Our home planet; inner rocky planet; only planet with liquid water and living things.", "149,600,000 km"),
    Planet(4, "Mars", "A dusty, cold, desert world with a thin atmosphere.", "227,900,000 km"),
    Planet(5, "Jupiter", "The largest planet in our solar system.", "778,600,000 km"),
    Planet(6, "Saturn", "Adorned with icy rings; gas planet.", "1,433,500,000 km"),
    Planet(7, "Uranus", "Seventh planet from the sun; rotates at nearly 90° degrees.", "2,872,500,000 km"),
    Planet(8, "Neptune", "The most distant planet; dark, cold, and with supersonic winds.", "4,495,100,000 km")
]

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["GET"])
def all_planet_facts():
    planets_response = []
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "distance from sun in km": planet.distance_from_sun_in_km
            }
        )

    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def planet_facts(planet_id):
    planet_id = int(planet_id)
    for planet in planets:
        if planet.id == planet_id:
            return {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "distance from sun in km": planet.distance_from_sun_in_km
            }
    return 404, "404 Not Found"