class NotFoundError(Exception):
    pass


class Route(object):
    def __init__(self, route_string):
        self._route_elems = [elem for elem in route_string.split('/') if elem != '']
        if route_string == '/':
            self._template = 'index.tpl'
        else:
            self._template = '{}.tpl'.format(route_string.strip('/').replace('/', '-'))

    def matches_uri(self, uri):    # return bool
        uri_elems = [elem for elem in uri.split('/') if elem != '']

        if len(uri_elems) != len(self._route_elems):
            return False

        for i in range(len(uri_elems)):
            if self._route_elems[i][0] == '[':
                continue
            if self._route_elems[i] != uri_elems[i]:
                return False
        return True

    @property
    def template(self):
        return self._template


class Router(object):
    def __init__(self):
        route_str = []
        with open('Router/routes.conf', 'r') as conf:
            for route in conf:
                route_str.append(route.strip('\n'))
        self.routes = [Route(string) for string in route_str]

    def route_for_uri(self, uri):
        for route in self.routes:
            if route.matches_uri(uri):
                return route
        raise NotFoundError
