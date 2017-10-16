#!/usr/bin/env python
# -*- coding: utf-8 -*-

from axure_requirements.utils.urls import include

urls = []

urls += include(r'/axure/', 'axure_requirements.handlers.axure.urls')
