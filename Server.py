from jinja2 import Environment, PackageLoader, Template, select_autoescape
from wsgiref.simple_server import make_server

from Router.Router import Router, NotFoundError

ROUTER = Router()


def application(environ, start_response):
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/html'),
    ]

    j2_env = Environment(loader=PackageLoader(__name__, 'Templates'),
                         autoescape=select_autoescape(['html', 'xml']),
                         )
    try:
        route = ROUTER.route_for_uri(environ['PATH_INFO'])
        template = j2_env.get_template(route.template)
    except NotFoundError:
        status = '404 Not Found'
        template = j2_env.get_template('404.tpl')

    start_response(status, response_headers)
    resp = template.render().encode('utf-8')

    return [resp]


httpd = make_server('', 8000, application)
print("Serving HTTP on port 8000...")
httpd.serve_forever()