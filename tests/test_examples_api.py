import requests
import logging


LOGGER = logging.getLogger(__name__)


def test_examples_api():
    response = requests.get("https://reqres.in/api/users?page=2")
    LOGGER.info(f'GET list users: {response.json()}')  # 1
    assert response.status_code == 200

    response = requests.get("https://reqres.in/api/users/2")
    LOGGER.info(f'GET single user: {response.json()}')  # 2
    assert response.status_code == 200

    response = requests.get("https://reqres.in/api/users/23")
    LOGGER.info(f'GET single user not found: {response.json()}')  # 3
    assert response.status_code == 404

    response = requests.get("https://reqres.in/api/unknown")
    LOGGER.info(f'GET list <resource>: {response.json()}')  # 4
    assert response.status_code == 200

    response = requests.get("https://reqres.in/api/unknown/2")
    LOGGER.info(f'GET single <resource>: {response.json()}')  # 5
    assert response.status_code == 200

    response = requests.get("https://reqres.in/api/unknown/23")
    LOGGER.info(f'GET single <resource> not found: {response.json()}')  # 6
    assert response.status_code == 404

    response = requests.post("https://reqres.in/api/users")
    LOGGER.info(f'POST create: {response.json()}')  # 7
    assert response.status_code == 201

    response = requests.put("https://reqres.in/api/users/2")
    LOGGER.info(f'PUT update: {response.json()}')  # 8
    assert response.status_code == 200

    response = requests.patch("https://reqres.in/api/users/2")
    LOGGER.info(f'PATCH update: {response.json()}')  # 9
    assert response.status_code == 200

    response = requests.delete("https://reqres.in/api/users/2")
    LOGGER.info(f'DELETE delete: {"Json должен отсутствовать"}')  # 10  # response.json()
    assert response.status_code == 204

    successful_params = {"email": "eve.holt@reqres.in", "password": "pistol"}
    response = requests.post("https://reqres.in/api/register", params=successful_params)
    LOGGER.info(f'POST register - successful: {response.json()}')  # 11  # <== [200 != 400]
    assert response.status_code == 200

    unsuccessful_params = {"email": "sydney@fife"}
    response = requests.post("https://reqres.in/api/register", params=unsuccessful_params)
    LOGGER.info(f'POST register - unsuccessful: {response.json()}')  # 12
    assert response.status_code == 400

    successful_params = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post("https://reqres.in/api/register", params=successful_params)
    LOGGER.info(f'POST login - successful: {response.json()}')  # 13
    assert response.status_code == 200

    unsuccessful_params = {"email": "peter@klaven"}
    response = requests.post("https://reqres.in/api/register", params=unsuccessful_params)
    LOGGER.info(f'POST login - unsuccessful: {response.json()}')  # 14
    assert response.status_code == 400

    response = requests.get("https://reqres.in/api/users?delay=3")
    LOGGER.info(f'GET delayed response: {response.json()}')  # 15
    assert response.status_code == 400
