from apistar import Route, Include
from apistar.handlers import docs_urls, serve_static, static_urls

from project.views import index, update, create, check, \
                          list_environments, health, delete

ROUTES = [
    Route('/', 'GET', index),
    Route('/environments/', 'GET', list_environments),
    Route('/environments/{slug}', 'GET', check),
    Route('/environments/{slug}', 'PUT', update),
    Route('/environments/{slug}', 'DELETE', delete),
    Route('/environments/', 'POST', create),
    Route('/health/', 'GET', health),
    Route('/statics/{path}', 'GET', serve_static),
    Include('/docs', docs_urls),
]
