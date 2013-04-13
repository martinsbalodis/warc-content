import os
import cherrypy
import json

class Links(object):

    def __init__(self, urltree):
        self.urls = json.dumps(urltree.urltree)

    @cherrypy.expose
    def links(self, node=None):
        return self.urls


def run(urltree):
    PATH = os.path.abspath(os.path.dirname(__file__))

    cherrypy.tree.mount(Links(urltree), '/', config={
        '/': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.join(PATH, 'static'),
            'tools.staticdir.index': 'index.html',
            },
        })

    cherrypy.engine.start()
    cherrypy.engine.block()
