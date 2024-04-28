from rest_framework import serializers
from .models import *

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True)
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password', 'messages']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
        