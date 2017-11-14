"""conftest module provides config to pytest to push results to server."""
import os
import pytest
import requests
from _pytest.runner import runtestprotocol

BASE_URL = os.getenv("ENVSTATUS_BASE_URL")


def get_env_name_from_test(test_name :str):
    # TODO Tests
    return test_name[5:-12].replace('_', ' ').capitalize()


def get_slug_from_test_name(test_name):
    # TODO Tests
    return test_name[5:-12]


def create_new_environment_from_test_name(test_name :str):
    # Create new environment from test name
    # e.g test_party_validation_environment bcomes Party Validation
    response = requests.post(f"{BASE_URL}/create/", 
                             data=dict(env_name=get_env_name_from_test(test_name)))
    assert response.status_code == 200


def _update_dashboard(name :str, result :str):
    """ Function to post update to dashboard """
    url = f"{os.getenv('ENVSTATUS_BASE_URL')}/update/{get_slug_from_test_name(name)}"
    print(f"Updating dashboard at {url}...")
    response = requests.put(url, data=dict(status=result))
    if response.status_code == 404:
        create_new_environment_from_test_name(name)
    else:
        assert response.status_code == 204


def pytest_runtest_protocol(item, nextitem):s
    """ After each test, report result to """
    reports = runtestprotocol(item, nextitem=nextitem)
    for report in reports:
        if report.when == 'call':
            if "environment" in item.name:
                print(f"{item.name} is {report.passed}")
                _update_dashboard(item.name, report.passed)
    return True
