# conftest.py
import pytest
from sqlalchemy import create_engine
from foo import models


@pytest.fixture(scope='session')
def connection(request):
    engine = create_engine('postgresql://bar@/test_bar')
    models.Base.metadata.create_all(engine)
    connection = engine.connect()
    models.DBSession.registry.clear()
    models.DBSession.configure(bind=connection)
    models.Base.metadata.bind = engine
    request.addfinalizer(models.Base.metadata.drop_all)
    return connection


@pytest.fixture
def db_session(request, connection):
    from transaction import abort
    trans = connection.begin()
    request.addfinalizer(trans.rollback)
    request.addfinalizer(abort)

    from foo.models import DBSession
    return DBSession