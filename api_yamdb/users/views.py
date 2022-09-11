from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.models import User
from users.permissions import OwnerOrAdmins
from users.serializers import (MeSerializer, SignUpSerializer, TokenSerializer,
                               UserSerializer)
from rest_framework_simplejwt.tokens import AccessToken


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    permission_classes = (OwnerOrAdmins, )
    filter_backends = (filters.SearchFilter, )
    filterset_fields = ('username')
    search_fields = ('username', )
    lookup_field = 'username'

    @action(
        methods=['get', 'patch'],
        detail=False,
        url_path='me',
        permission_classes=(IsAuthenticated, )
    )
    def get_patch_me(self, request):
        user = get_object_or_404(User, username=self.request.user)
        if request.method == 'GET':
            serializer = MeSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == 'PATCH':
            serializer = MeSerializer(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def signup_post(request):
    serializer = SignUpSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.validated_data['email']
    username = serializer.validated_data['username']
    if username == 'me':
        return Response('Логин "me" использовать нельзя',
                        status=status.HTTP_400_BAD_REQUEST)
    try:
        user, created = User.objects.get_or_create(
            username=username,
            email=email,
        )
    except IntegrityError:
        return Response(
            'Пользователь с таким логином или email уже существует',
            status=status.HTTP_400_BAD_REQUEST
        )
    confirmation_code = default_token_generator.make_token(user)

    send_mail(
        'Код подверждения',
        confirmation_code,
        'admin@email.com',
        [email],
        fail_silently=False
    )
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def token_post(request):
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data['username']
    confirmation_code = serializer.validated_data['confirmation_code']
    user = get_object_or_404(User, username=username)
    if confirmation_code != user.confirmation_code:
        return Response(
            {'confirmation_code': 'Неверный код подтверждения'},
            status=status.HTTP_400_BAD_REQUEST
        )
    token = AccessToken.for_user(user)
    return Response({f'token: {token}'}, status=status.HTTP_200_OK)
