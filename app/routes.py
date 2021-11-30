from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, request, make_response


# class Planet:
#     def __init__(self, id, name, description, distance_from_sun_in_km, moon_count):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.distance_from_sun_in_km = distance_from_sun_in_km
#         self.moon_count = moon_count

# planets = [
#     Planet(1, "Mercury", "The smallest and fastest planet; inner rocky planet.", "57,900,000 km", "0"),
#     Planet(2, "Venus", "The hottest planet in our solar system.", "108,200,000 km", "0"),
#     Planet(3, "Earth", "Our home planet; inner rocky planet; only planet with liquid water and living things.", "149,600,000 km", "1"),
#     Planet(4, "Mars", "A dusty, cold, desert world with a thin atmosphere.", "227,900,000 km", "2"),
#     Planet(5, "Jupiter", "The largest planet in our solar system.", "778,600,000 km", "79 (53 Confirmed, 26 Provisional)"),
#     Planet(6, "Saturn", "Adorned with icy rings; gas planet.", "1,433,500,000 km", "82 (53 Confirmed, 29 Provisional"),
#     Planet(7, "Uranus", "Seventh planet from the sun; rotates at nearly 90° degrees.", "2,872,500,000 km", "27"),
#     Planet(8, "Neptune", "The most distant planet; dark, cold, and with supersonic winds.", "4,495,100,000 km", "14")
# ]

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["POST", "GET"])
def handle_planets():
    if request.method == "POST":

        request_body = request.get_json()
        if "name" not in request_body or "description" not in request_body \
                or "distance_from_sun_in_km" not in request_body \
                or "moon_count" not in request_body:

            return make_response("Invalid Request", 400)

        new_planet = Planet(
            name=request_body["name"],
            description=request_body["description"],
            distance_from_sun_in_km=request_body["distance_from_sun_in_km"],
            moon_count=request_body["moon_count"]
        )

        db.session.add(new_planet)
        db.session.commit()

        new_planet_response = {
            "id": new_planet.id,
            "name": new_planet.name,
            "description": new_planet.description,
            "distance_from_sun_in_km": int(new_planet.distance_from_sun_in_km),
            "moon_count": new_planet.moon_count
        }

        # return make_response(f"Planet {new_planet.name} with id: {new_planet.id} successfully created", 201)
        return jsonify(new_planet_response), 201

    elif request.method == "GET":
        name_query = request.args.get("name")
        description_query = request.args.get("description")
        distance_from_sun_query = request.args.get("distance_from_sun_in_km")
        moon_count_query = request.args.get("moon_count")

        if name_query:
            planets = Planet.query.filter(
                Planet.name.contains(name_query))  # Case Sensitve
        elif description_query:
            planets = Planet.query.filter(
                Planet.description.contains(description_query))
        elif distance_from_sun_query:
            planets = Planet.query.filter(
                Planet.distance_from_sun_in_km.contains(distance_from_sun_query))
        elif moon_count_query:
            planets = Planet.query.filter(
                Planet.moon_count.contains(moon_count_query))
        else:
            planets = Planet.query.all()

        planets_response = []
        for planet in planets:
            planets_response.append(
                {
                    "id": planet.id,
                    "name": planet.name,
                    "description": planet.description,
                    # converted numeric to integer
                    "distance_from_sun_in_km": int(planet.distance_from_sun_in_km),
                    "moon_count": planet.moon_count
                }
            )

        return jsonify(planets_response)


@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def planet_facts(planet_id):
    planet = Planet.query.get(planet_id)

    if planet is None:
        return jsonify(planet_id), 404

    if request.method == "GET":
        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "distance_from_sun_in_km": int(planet.distance_from_sun_in_km),
            "moon_count": planet.moon_count
        }

    elif request.method == "PUT":
        if planet is None:
            return jsonify(planet_id), 404

        request_body = request.get_json()
        if "name" not in request_body or "description" not in request_body:
            return make_response("Invalid Request", 400)

        planet.name = request_body["name"]
        planet.description = request_body["description"]

        db.session.commit()

        return jsonify(planet_id), 201

    elif request.method == "DELETE":
        if planet is None:
            return jsonify(planet_id), 404

        db.session.delete(planet)
        db.session.commit()

        return jsonify(planet_id), 200
