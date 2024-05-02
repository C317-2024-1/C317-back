from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
import jwt, datetime 

from api.models import User
from api.serializers import UserSerializer
from rest_framework.decorators import api_view
from api.utils import *

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.filter(email=email).first()

        if user is None or not user.check_password(password):
            return Response({
                'message': 'Check your email or password'
            })

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=120),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload,'c317-scret-key', algorithm='HS256')

        response = Response()

        response.set_cookie(key='c317-jwt', value=token, httponly=True)

        response.data = {
            'c317-jwt': token
        }

        return response

@api_view(['GET'])
def user(request):

    user_id = get_user_id_by_jwt(request)


    if 'error' in user_id:
        return Response(user_id, status=status.HTTP_401_UNAUTHORIZED)


    user = User.objects.filter(id=user_id['id']).first()
    user_serializer = UserSerializer(user)
    return Response(user_serializer.data)

@api_view(['POST'])
def logout(resquest):
    response = Response()
    response.delete_cookie('c317-jwt')
    response.data = {
        "messages": 'Successfully logged out'
    }
    return response

@api_view(['POST'])
def message_handler(request):
    if request.method == 'POST':
        if request.data.get('message') == '':
            return Response({'message': 'Message cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)

        user_id = get_user_id_by_jwt(request)
        if 'error' in user_id:
            return Response(user_id, status=status.HTTP_401_UNAUTHORIZED)
        
        message = {
            'message': request.data.get('message'),
            'date': datetime.datetime.now(),
            'isUserMessage': True
        }

        user = save_message(user_id['id'], message)         
        
        ai_response = get_ai_response(user_id['id'], message['message'])

        if user is None:
            return Response({'message': 'An error occurred'}, status=status.HTTP_400_BAD_REQUEST)
        

        return Response(ai_response.data, status.HTTP_201_CREATED)

@api_view(['GET'])
def user_messages(request):
    user_id = get_user_id_by_jwt(request)
    if 'error' in user_id:
        return Response(user_id, status=status.HTTP_401_UNAUTHORIZED)

    user = User.objects.filter(id=user_id['id']).first()
    user_messages = user.messages

    return Response(user_messages)