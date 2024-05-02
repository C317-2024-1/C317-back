
import jwt
import datetime
from rest_framework.response import Response
from rest_framework import status
from .models import User

def get_user_id_by_jwt(request):
    token = request.COOKIES.get('c317-jwt')
    if not token:
        return {'error': 'User not authenticated'}
    try:
        payload = jwt.decode(token, 'c317-scret-key', algorithms=['HS256'])
        return {'id': payload['id']}
    except jwt.ExpiredSignatureError:
        return {'error': 'Token expired'}

def save_message(user_id, message):
    user = User.objects.filter(id=user_id).first()
    user.messages.append(message)
    user.save()

    if user is None:
        return Response({'message': 'An error occurred connecting to DB'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_200_OK)

def get_ai_response(user_id, message):
    '''
    Will contain the logic to generate a response from the AI
    '''

    ai_response = {
        'message': 'Hello, I am an AI',
        'date': datetime.datetime.now(),
        'isUserMessage': False
    }

    if ai_response is None:
        return Response({'message': 'An error occurred trying to consume AI'}, status=status.HTTP_400_BAD_REQUEST)
    save_message(user_id, ai_response)

    return Response(ai_response, status=status.HTTP_200_OK)
    
    