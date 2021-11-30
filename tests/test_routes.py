# Get all planets and return no records
def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

# Get one planet by id


def test_get_planet_by_id(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Water Planet",
        "description": "Where the ocean is worshipped as a divine entity.",
        "distance_from_sun_in_km": 149600000,
        "moon_count": 1
    }

# Test no data in test database returns 404


def test_get_planet_by_id_with_no_data(client):
    # Act
    response = client.get("/planet/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == None

# Valid test data returns 200 with an array including appropriate test data


def test_get_valid_data_with_all_records(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [
        {
            "id": 1,
            "name": "Water Planet",
            "description": "Where the ocean is worshipped as a divine entity.",
            "distance_from_sun_in_km": 149600000,
            "moon_count": 1
        },
        {
            "id": 2,
            "name": "Windy Planet",
            "description": "The most distant planet; dark, cold, and with supersonic winds.",
            "distance_from_sun_in_km": 4495100000,
            "moon_count": 14
        }
    ]

# POST/planets with a JSON request body returns 201


def test_post_with_json_request_body(client):
    # Act
    response = client.post("/planets",  json={
        "name": "Gas Planet",
        "description": "The largest planet in our solar system.",
        "distance_from_sun_in_km": 778600000,
        "moon_count": 79
    }
    )
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "Gas Planet",
        "description": "The largest planet in our solar system.",
        "distance_from_sun_in_km": 778600000,
        "moon_count": 79
    }
