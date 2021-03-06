from chaussette.backend import _wsgiref

_backends = {'wsgiref': _wsgiref.ChaussetteServer}

try:
    from chaussette.backend import _gevent
    _backends['gevent'] = _gevent.Server

    from chaussette.backend import _fastgevent
    _backends['fastgevent'] = _fastgevent.Server
except ImportError:
    pass


try:
    from chaussette.backend import _meinheld
    _backends['meinheld'] = _meinheld.Server
except ImportError:
    pass


try:
    from chaussette.backend import _waitress
    _backends['waitress'] = _waitress.Server
except ImportError:
    pass


def register(name, server):
    _backends[name] = server


def get(name):
    return _backends[name]


def backends():
    return _backends.keys()
