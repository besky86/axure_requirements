#!/usr/bin/env python
# -*- coding=utf-8 -*-

from tornado.web import URLSpec as url, StaticFileHandler

from .views import AxureHandler

import os.path
up_dir = os.path.dirname(__file__)
count = 5
for i in range(4):
    requirement_dir = os.path.join(up_dir, '../project_requirements')
    if os.path.isdir(requirement_dir):
        up_dir = requirement_dir
        break
    else:
        up_dir = os.path.join(up_dir, '../')
requirement_dir = os.path.abspath(up_dir)

urls = [
    url(r'', AxureHandler),
    url(r'/(.*)', StaticFileHandler, {'path':requirement_dir}),
]
