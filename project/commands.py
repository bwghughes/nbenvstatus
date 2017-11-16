from apistar.backends.sqlalchemy_backend import Session
from project.models import ApplicationStatus

def create_envs(session: Session):
        """ Create a group of environments for testing. """
        for app in ['MDM', 'Nedbank ID', 'ECM', 'Credit Decision Engine', 'Arrangement',
                'Party', 'AEM', 'Product Catalogue', 'Dirty Cache', 'EWCO']:
                app_status = ApplicationStatus(name=app)
                session.add(app_status)
                print(f'Environment {app_status.name} added with slug {app_status.slug}')
                session.flush()
