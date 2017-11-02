from apistar import Route, Include
from apistar.handlers import docs_urls, serve_static, static_urls

from project.views import index, update

ROUTES = [
    Route('/', 'GET', index),
    Route('/update/{status_id}', 'PUT', update),
    Route('/static/{path}', 'GET', serve_static),
    Include('/docs', docs_urls),
]
