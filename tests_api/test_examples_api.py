import requests
import logging
from asserts.for_test_examples_api import *


LOGGER = logging.getLogger(__name__)


def test_get_list_users():
    response = requests.get("https://reqres.in/api/users?page=2")
    LOGGER.info('GET list users')
    assert response.status_code == 200
    assert response.json() == get_list_users_json
    return response.status_code, response.json()


def test_get_single_user():
    response = requests.get("https://reqres.in/api/users/2")
    LOGGER.info('GET single user')
    assert response.status_code == 200
    assert response.json() == get_single_user_json
    return response.status_code, response.json()


def test_get_single_user_not_found():
    response = requests.get("https://reqres.in/api/users/23")
    LOGGER.info('GET single user not found')
    assert response.status_code == 404
    assert response.json() == {}
    return response.status_code, response.json()


def test_get_list_resource():
    response = requests.get("https://reqres.in/api/unknown")
    LOGGER.info('GET list <resource>')
    assert response.status_code == 200
    assert response.json() == get_list_resource_json
    return response.status_code, response.json()


def test_get_single_resource():
    response = requests.get("https://reqres.in/api/unknown/2")
    LOGGER.info('GET single <resource>')
    assert response.status_code == 200
    assert response.json() == get_single_resource_json
    return response.status_code, response.json()


def test_get_single_resource_not_found():
    response = requests.get("https://reqres.in/api/unknown/23")
    LOGGER.info('GET single <resource> not found')
    assert response.status_code == 404
    assert response.json() == {}
    return response.status_code, response.json()


def test_post_create():
    post_create_json_param = {
        "name": "morpheus",
        "job": "leader"
    }
    response = requests.post("https://reqres.in/api/users", json=post_create_json_param)
    LOGGER.info('POST create')
    assert response.status_code == 201
    assert response.json()['name'] == 'morpheus' and response.json()['job'] == 'leader'
    return response.status_code, response.json()


def test_put_update():
    put_update_json_param = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = requests.put("https://reqres.in/api/users/2", json=put_update_json_param)
    LOGGER.info('PUT update')
    assert response.status_code == 200
    assert response.json()['name'] == 'morpheus' and response.json()['job'] == 'zion resident'
    return response.status_code, response.json()


def test_patch_update():
    patch_update_json_param = {
        "name": "morpheus",
        "job": "zion resident"
    }
    response = requests.patch("https://reqres.in/api/users/2", json=patch_update_json_param)
    LOGGER.info('PATCH update')
    assert response.status_code == 200
    assert response.json()['name'] == 'morpheus' and response.json()['job'] == 'zion resident'
    return response.status_code, response.json()


def test_delete_delete():
    response = requests.delete("https://reqres.in/api/users/2")
    LOGGER.info('DELETE delete')
    assert response.status_code == 204
    assert response.content == b''
    return response.status_code, response.json()


def test_post_register_successful():
    post_register_successful_json_param = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = requests.post("https://reqres.in/api/register", json=post_register_successful_json_param)
    LOGGER.info('POST register - successful')
    assert response.status_code == 200
    assert response.json() == post_register_successful_json
    return response.status_code, response.json()


def test_post_register_unsuccessful():
    post_register_unsuccessful_json_param = {
        "email": "sydney@fife"
    }
    response = requests.post("https://reqres.in/api/register", json=post_register_unsuccessful_json_param)
    LOGGER.info('POST register - unsuccessful')
    assert response.status_code == 400
    assert response.json() == post_register_unsuccessful_json
    return response.status_code, response.json()


def test_post_login_successful():
    post_login_successful_json_param = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post("https://reqres.in/api/register", json=post_login_successful_json_param)
    LOGGER.info('POST login - successful')
    assert response.status_code == 200
    assert response.json() == post_login_successful_json  # в api появилось новое занчение - id
    return response.status_code, response.json()


def test_post_login_unsuccessful():
    post_login_unsuccessful_json_param = {
        "email": "peter@klaven"
    }
    response = requests.post("https://reqres.in/api/register", json=post_login_unsuccessful_json_param)
    LOGGER.info('POST login - unsuccessful')
    assert response.status_code == 400
    assert response.json() == post_register_unsuccessful_json
    return response.status_code, response.json()


def test_get_delayed_response():
    response = requests.get("https://reqres.in/api/users?delay=3")
    LOGGER.info('GET delayed response')
    assert response.status_code == 200
    assert response.json() == get_delayed_response_json
    return response.status_code, response.json()
