""" Views, includes HTML and API """
import typing
from datetime import datetime

from apistar import Response, annotate, render_template
from apistar.backends.sqlalchemy_backend import Session
from apistar.renderers import HTMLRenderer, JSONRenderer

from project.models import ApplicationStatus


@annotate(renderers=[HTMLRenderer()])
def index(session: Session):
    """ Home view. """
    statuses = session.query(ApplicationStatus)
    return render_template('index.html', envstatus=statuses)


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



def update(session: Session, slug: str, status: bool):
    """ Update the status """
    status = session.query(ApplicationStatus).filter_by(slug=slug).first()
    status.status = True
    status.last_updated = datetime.now()
    session.commit()
    return Response(status=204)


@annotate(renderers=[JSONRenderer()])
def create(session: Session, name: str):
    """ Create new """
    if name:
        status = ApplicationStatus(name=name)
        session.add(status)
        session.flush()
        return {'name': status.name, 'status': status.status, 'slug': status.slug}
    else:
        return Response(status=400)
