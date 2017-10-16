#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.web import RequestHandler

class AxureHandler(RequestHandler):
    
    def get(self):
        self.write('test')
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
        requirements_list = list()
        for each_path in os.listdir(requirement_dir):
            start_path = os.path.join(requirement_dir, each_path)
            if os.path.isdir(start_path):
                start_html_path = os.path.join(each_path, 'start.html')
                if os.path.isfile(os.path.join(start_path, 'start.html')):
                    requirements_list.append((os.path.basename(each_path), start_html_path))
        print requirements_list
        self.render('axure/project.html', project_list=requirements_list)


    def get_start_html(self):
        pass






