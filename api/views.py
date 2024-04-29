from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
import jwt, datetime 

from api.models import User, Message
from api.serializers import UserSerializer, MessageSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        user = request.query_params.get('name', None)
        if user is not None:
            users = users.filter(name__icontains=user)
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False, status=status.HTTP_200_OK)

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

    token = request.COOKIES.get('c317-jwt')

    if not token:
        return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        payload = jwt.decode(token, 'c317-scret-key', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return Response({'error': 'Token expired'}, status=status.HTTP_401_UNAUTHORIZED)

    user = User.objects.filter(id=payload['id']).first()
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