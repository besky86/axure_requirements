#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import os

from tornado.web import RequestHandler
from .conf import REQUIREMENTS_PATH

class AxureHandler(RequestHandler):

    def get(self):
        requirement_dir = REQUIREMENTS_PATH if REQUIREMENTS_PATH else self.get_requirements_path()

        if not requirement_dir:
            self.write('请在环境变量中设置需求所在目录')
            return

        requirements_list = list()
        for each_path in os.listdir(requirement_dir):
            start_path = os.path.join(requirement_dir, each_path)
            if os.path.isdir(start_path):
                start_html_path = os.path.join(each_path, 'start.html')
                if os.path.isfile(os.path.join(start_path, 'start.html')):
                    requirements_list.append((os.path.basename(each_path), start_html_path))
        if requirements_list:
            self.render('axure/project.html', project_list=requirements_list)
        else:
            self.write('not requirements')

    def get_requirements_path(self):
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
        return requirement_dir

    def get_start_html(self):
        pass






