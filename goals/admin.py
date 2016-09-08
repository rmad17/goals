# -*- coding: utf-8 -*-
#
# Copyright © 2016 rmad17 <souravbasu17@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Admin Panel related functionality
"""

from django.contrib import admin
from .models import Goal


admin.site.register(Goal)
