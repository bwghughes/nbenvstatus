""" Views, includes HTML and API """
import os
import typing
from datetime import datetime
import arrow

from apistar import Response, annotate, render_template
from apistar.backends.sqlalchemy_backend import Session
from apistar.renderers import HTMLRenderer, JSONRenderer

from project.models import ApplicationStatus


@annotate(renderers=[HTMLRenderer()])
def index(session: Session) -> Response:
    """ Home view. """
    statuses = session.query(ApplicationStatus)
    context = {'envstatus': statuses, 
               'arrow': arrow,
               'page_name': os.getenv('PAGE_NAME')}
    return render_template('index.html', **context)


@annotate(renderers=[JSONRenderer()])
def check(session: Session, slug: str) -> Response:
    """ Update the status """
    status = session.query(ApplicationStatus).filter_by(slug=slug).first()
    if status:  
        return {'name': status.name, 'status': status.status}
    else:
        return Response(status=404)


@annotate(renderers=[JSONRenderer()])
def list_environments(session: Session) -> typing.List[ApplicationStatus]:
    statuses = session.query(ApplicationStatus).all()
    return [status.to_dict() for status in statuses]



def update(session: Session, slug: str, test_result: bool) -> Response:
    """ Update the status """
    status = session.query(ApplicationStatus).filter_by(slug=slug).first()
    print(f"Updating {status} with {test_result}...")
    status.status = test_result
    status.last_updated = datetime.now()
    session.commit()
    return Response(status=204)


@annotate(renderers=[JSONRenderer()])
def create(session: Session, name: str) -> Response:
    """ Create new """
    if name:
        status = ApplicationStatus(name=name.upper())
        session.add(status)
        session.flush()
        return {'name': status.name, 'status': status.status, 'slug': status.slug}
    else:
        return Response(status=400)
