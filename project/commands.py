from apistar.backends.sqlalchemy_backend import Session
from project.models import ApplicationStatus

def create_envs(session: Session):
        """ Create a group of environments for testing. """
        for app in ['MDM', 'Nedbank ID', 'ECM', 'Credit Decision Engine', 'Arrangement',
                'Party', 'AEM', 'Product Catalogue', 'Dirty Cache', 'EWCO']:
                app_status = ApplicationStatus(group='E2E', name=app)
                session.add(app_status)
                print(f'Environment {app_status.name} added to E2E with slug {app_status.slug}')
                session.flush()


def create_env(session: Session, group: str, name: str):
        """ Create a single environment. Group and Name are required. """
        app_status = ApplicationStatus(group=group, name=name)
        session.add(app_status)
        session.flush()
        print(f'Environment {name} added to {group}')

