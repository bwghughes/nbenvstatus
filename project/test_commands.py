""" Test for commands.py """
import pytest
from unittest.mock import MagicMock, patch
from project.commands import create_envs

@pytest.fixture
def mock_session():
    return MagicMock()


def test_create_env(mock_session):
    p = create_envs(mock_session)
    #assert mock_session.called
    assert False
    