# -*- coding: utf-8 -*-
#
# Copyright © 2016 rmad17 <souravbasu17@gmail.com>
#
# Distributed under terms of the MIT license.

"""
All operations on models
"""

from django.db import IntegrityError
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token

from .models import Goal


def insert_goal(user, title, target_date, description=None):
    if not user and title and target_date:
        return None
    try:
        goal = Goal(user=user, title=title, description=description,
                    target_date=target_date)
        goal.save()
        return goal
    except IntegrityError as e:
        return e.__cause__


def create_token(user):
    if not user:
        return None
    try:
        token = Token.objects.create(user=user)
        token.save()
        return token
    except IntegrityError as e:
        return e.__cause__


def get_user_by_username(user_name):
    try:
        return User.objects.get(username=user_name)
    except IntegrityError:
        return None


def get_token_by_user(user):
    try:
        return Token.objects.get(user=user)
    except IntegrityError as e:
        return e.__cause__


def get_all_goals():
    return Goal.objects.all()


def get_goal_by_uuid(uuid):
    try:
        return Goal.objects.get(uuid=uuid)
    except Goal.DoesNotExist:
        return None


def get_goals_by_user(user):
    try:
        return Goal.objects.filter(user=user)
    except Goal.DoesNotExist:
        return None
