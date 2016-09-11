# -*- coding: utf-8 -*-
#
# Copyright © 2016 rmad17 <souravbasu17@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Serializers for Django Rest Framework
"""
from django.contrib.auth.models import User, Group

from rest_framework import serializers

from .models import Goal
from .modelops import create_token


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ('uuid', 'created_at', 'user', 'title', 'description',
                  'target_date', 'end_date')

    def create(self, validated_data):
        """
        Create and return a new `Goal` instance, given the validated data.
        """
        return Goal.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Goal` instance, given the validated data
        """
        instance.user = validated_data.get('user', instance.user)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description',
                                                  instance.description)
        instance.target_date = validated_data.get('target_date',
                                                  instance.target_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.save()
        return instance


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(write_only=True)
    goals = GoalSerializer(many=True, read_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name')
        )
        user.set_password(validated_data.get('password'))
        user.save()
        create_token(user)
        return user

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'goals',)
