from apistar import Route, Include
from apistar.handlers import docs_urls, serve_static, static_urls

from project.views import index, update, create, check

ROUTES = [
    Route('/', 'GET', index),
    Route('/{slug}', 'GET', check),
    Route('/update/{slug}', 'PUT', update),
    Route('/create/', 'POST', create),
    Route('/static/{path}', 'GET', serve_static),
    Include('/docs', docs_urls),
]
