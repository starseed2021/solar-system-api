import pytest
from app import create_app
from app import db
from app.models.planet import Planet


@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_planets(app):
    # Arrange
    water_planet = Planet(
        name = "Water Planet",
        description = "Where the ocean is worshipped as a divine entity.",
        distance_from_sun_in_km = 149600000,
        moon_count = 1
    )
    windy_planet = Planet(
        name = "Windy Planet",
        description = "The most distant planet; dark, cold, and with supersonic winds.",
        distance_from_sun_in_km = 4495100000,
        moon_count = 14
    )

    db.session.add_all([water_planet, windy_planet]) # Allows you to add all items at once
    # Alternatively, we could do
    # db.session.add(ocean_book)
    # db.session.add(food_book)
    db.session.commit()