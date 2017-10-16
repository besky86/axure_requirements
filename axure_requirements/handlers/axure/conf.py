#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
from os.path import expanduser

bash_rc = ''
if os.path.exists(expanduser("~/.bashrc")):
    with open(expanduser("~/.bashrc")) as f:
        bash_rc += f.read()

if os.path.exists(expanduser("~/.bash_profile")):
    with open(expanduser("~/.bash_profile")) as f:
        bash_rc += f.read()

match = re.search(r'REQUIREMENTS_PATH=(.+)', bash_rc)
REQUIREMENTS_PATH = match.group(1) if match else ''

