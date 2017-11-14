"""conftest module provides config to pytest to push results to server."""
import os
import pytest
import requests
from _pytest.runner import runtestprotocol

BASE_URL = os.getenv("ENVSTATUS_BASE_URL")


def get_slug_from_test_name(test_name):
    return test_name[5:-12]


def _update_dashboard(name, result):
    """ Function to post update to dashboard """
    url = f"{os.getenv('ENVSTATUS_BASE_URL')}/update/{get_slug_from_test_name(name)}"
    print(f"Updating dashboard at {url}...")
    response = requests.put(url, data=dict(status=result))
    assert response.status_code == 204


def pytest_runtest_protocol(item, nextitem):
    """ After each test, report result to """
    reports = runtestprotocol(item, nextitem=nextitem)
    for report in reports:
        if report.when == 'call':
            if "environment" in item.name:
                print(f"{item.name} is {report.passed}")
                _update_dashboard(item.name, report.passed)
    return True
