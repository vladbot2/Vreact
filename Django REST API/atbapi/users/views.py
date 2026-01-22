import requests
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def google_login(request):
    token = request.data.get('token')

    if not token:
        return Response({'error': 'no token'}, status=400)

    google_url = 'https://www.googleapis.com/oauth2/v3/userinfo'
    headers = {
        'Authorization': f'Bearer {token}'
    }

    r = requests.get(google_url, headers=headers)

    if r.status_code != 200:
        return Response({'error': 'google error'}, status=400)

    data = r.json()

    email = data.get('email')
    first_name = data.get('given_name', '')
    last_name = data.get('family_name', '')

    if not email:
        return Response({'error': 'no email'}, status=400)

    user, created = User.objects.get_or_create(
        username=email,
        defaults={
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
        }
    )

    token_obj, _ = Token.objects.get_or_create(user=user)

    return Response({
        'token': token_obj.key,
        'email': user.email,
    })
