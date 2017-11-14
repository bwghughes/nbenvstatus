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


def update(session: Session, slug: str, status: bool):
    """ Update the status """
    status = session.query(ApplicationStatus).filter_by(slug=slug).first()
    status.status = True
    status.last_updated = datetime.now()
    session.commit()
    return Response(status=204)


def create(session: Session, name: str):
    app_status = ApplicationStatus(name=name)
    session.add(app_status)
    print(f'Environment {app_status.name} added to E2E with slug {app_status.slug}')
    session.flush()
    return Response(status=200)
