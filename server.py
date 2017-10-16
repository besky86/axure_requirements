#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
from axure_requirements.handlers.urls import urls

class TestHandler(tornado.web.RequestHandler):
    
    def get(self):
        self.write("test handler")


def make_app():
    settings = {
        'static_path': 'axure_requirements/static',
        'template_path': 'axure_requirements/templates',
        'debug': True,
    }
    return tornado.web.Application(urls, **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
