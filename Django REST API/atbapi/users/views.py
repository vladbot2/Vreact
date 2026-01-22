<<<<<<< HEAD
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
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 0836948cd765c84e457c61238868684ca2780c47
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

<<<<<<< HEAD
from .serializers import LoginSerializer, RegisterSerializer, UserSerializer, PasswordResetRequestSerializer, SetNewPasswordSerializer
from rest_framework import parsers
from rest_framework_simplejwt.tokens import RefreshToken

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

=======
from .serializers import RegisterSerializer, UserSerializer
from rest_framework import parsers
from rest_framework_simplejwt.tokens import RefreshToken

>>>>>>> 0836948cd765c84e457c61238868684ca2780c47
from .models import CustomUser

class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    # Create your views here.
    @action(detail=False, methods=['post'], url_path='register', serializer_class=RegisterSerializer)
    def register(self, request):

        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            refresh = RefreshToken.for_user(user)

            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
<<<<<<< HEAD
    
    @action(detail=False, methods=['post'], url_path='login', serializer_class=LoginSerializer)
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = CustomUser.objects.filter(username=username)
            user = user.first()
            if not user:
                return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
            # if not user.exists():
            #     return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
            
            if user.check_password(password):
                refresh = RefreshToken.for_user(user)

                return Response(
                    {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return Response({"detail" : "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
            
    @action(detail=False, methods=['post'], url_path='forgot-password',serializer_class=PasswordResetRequestSerializer)
    def password_reset_request(self, request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"detail": "Лист для відновлення паролю відправлено"}, 
            status=status.HTTP_200_OK
        )
    
    @action(detail=False, methods=['post'], url_path='reset-password', serializer_class=SetNewPasswordSerializer)
    def password_reset_confirm(self, request):
        serializer = SetNewPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            uid = urlsafe_base64_decode(serializer.validated_data['uid']).decode()
            user = CustomUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            return Response({"detail": "Невірний uid"}, status=status.HTTP_400_BAD_REQUEST)

        if not default_token_generator.check_token(user, serializer.validated_data['token']):
            return Response({"detail": "Невірний або прострочений токен"}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(serializer.validated_data['new_password'])
        user.save()
        return Response({"detail": "Пароль успішно змінено"}, status=status.HTTP_200_OK)
=======
=======
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": "Реєстрація успішна"},
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
>>>>>>> 5f3157850eb87e28d70d2e6f1d58428d66ca0ed6
>>>>>>> 0836948cd765c84e457c61238868684ca2780c47
>>>>>>> 456b6310aad55a6943e785cf21b6c6f5a78ee605
