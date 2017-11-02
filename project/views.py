""" Views, includes HTML and API """
from datetime import datetime
from apistar import annotate, render_template, Response
from apistar.renderers import HTMLRenderer
from apistar.backends.sqlalchemy_backend import Session
from project.models import ApplicationStatus


@annotate(renderers=[HTMLRenderer()])
def index(session: Session):
    """ Home view. """
    statuses = session.query(ApplicationStatus)
    return render_template('index.html', envstatus=statuses)


def update(session: Session, status_id: int, status: bool):
    status = session.query(ApplicationStatus)\
             .get(status_id)
    status.status = True
    status.last_updated = datetime.now()
    session.commit()
    return Response(status=204)
