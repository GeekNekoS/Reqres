import requests
import logging
from asserts.for_test_examples_api import *


LOGGER = logging.getLogger(__name__)


def test_get_list_users():
    response = requests.get("https://reqres.in/api/users?page=2")
    LOGGER.info(f'GET list users')
    assert response.status_code == 200
    assert response.json() == get_list_users_json


def test_get_single_user():
    response = requests.get("https://reqres.in/api/users/2")
    LOGGER.info(f'GET single user')
    assert response.status_code == 200
    assert response.json() == get_single_user_json


def test_get_single_user_not_found():
    response = requests.get("https://reqres.in/api/users/23")
    LOGGER.info(f'GET single user not found')
    assert response.status_code == 404
    assert response.json() == {}


def test_get_list_resource():
    response = requests.get("https://reqres.in/api/unknown")
    LOGGER.info(f'GET list <resource>')
    assert response.status_code == 200
    assert response.json() == get_list_resource_json


def test_get_single_resource():
    response = requests.get("https://reqres.in/api/unknown/2")
    LOGGER.info(f'GET single <resource>')
    assert response.status_code == 200
    assert response.json() == get_single_resource_json


def test_get_single_resource_not_found():
    response = requests.get("https://reqres.in/api/unknown/23")
    LOGGER.info(f'GET single <resource> not found')
    assert response.status_code == 404
    assert response.json() == {}


def test_post_create():
    post_create_json = {
        "name": "morpheus",
        "job": "leader"
    }
    response = requests.post("https://reqres.in/api/users", json=post_create_json)
    LOGGER.info(f'POST create')
    assert response.status_code == 201
    assert response.json()['name'] == 'morpheus' and response.json()['job'] == 'leader'


def test_put_update():
    put_update_json = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = requests.put("https://reqres.in/api/users/2", json=put_update_json)
    LOGGER.info(f'PUT update')
    assert response.status_code == 200
    assert response.json()['name'] == 'morpheus' and response.json()['job'] == 'zion resident'


def test_patch_update():
    response = requests.patch("https://reqres.in/api/users/2")
    LOGGER.info(f'PATCH update: {response.json()}')
    assert response.status_code == 200  # <== Остановилась здесь


def test_examples_api():
    response = requests.delete("https://reqres.in/api/users/2")
    LOGGER.info(f'DELETE delete: {"Json должен отсутствовать"}')  # 10  # response.json()
    assert response.status_code == 204

    successful_params = {"email": "eve.holt@reqres.in", "password": "pistol"}
    response = requests.post("https://reqres.in/api/register", params=successful_params)
    LOGGER.info(f'POST register - successful: {response.json()}')  # 11
    assert response.status_code == 400  # 200

    unsuccessful_params = {"email": "sydney@fife"}
    response = requests.post("https://reqres.in/api/register", params=unsuccessful_params)
    LOGGER.info(f'POST register - unsuccessful: {response.json()}')  # 12
    assert response.status_code == 400

    successful_params = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post("https://reqres.in/api/register", params=successful_params)
    LOGGER.info(f'POST login - successful: {response.json()}')  # 13
    assert response.status_code == 400  # 200

    unsuccessful_params = {"email": "peter@klaven"}
    response = requests.post("https://reqres.in/api/register", params=unsuccessful_params)
    LOGGER.info(f'POST login - unsuccessful: {response.json()}')  # 14
    assert response.status_code == 400

    response = requests.get("https://reqres.in/api/users?delay=3")
    LOGGER.info(f'GET delayed response: {response.json()}')  # 15
    assert response.status_code == 200  # 400
