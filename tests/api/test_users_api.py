import requests


def test_get_users():

    response = requests.get("https://reqres.in/api/users?page=2")

    assert response.status_code == 200
    assert "data" in response.json()


def test_create_user():

    payload = {
        "name": "morpheus",
        "job": "leader"
    }

    response = requests.post(
        "https://reqres.in/api/users",
        json=payload
    )

    assert response.status_code == 201
    assert response.json()["name"] == "morpheus"