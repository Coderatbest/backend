# rest frameworks
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import action
# serializers
from users.serializers import (
    UsersSerializer,
    UsersLoginSerializer,
    UserSignUpSerializer,
    UserVerificationSerializer
    )
# models
from users.models import User

class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_activate=True)
    serializer_class = UsersSerializer
    #permission_classes = (IsAuthenticated,)
    lookup_field = 'username'
    """docs."""
    @action(detail=False,methods=['post'])
    def login(self,request):
        serializer = UsersLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user,token = serializer.save()
        return Response({
            'user': UsersSerializer(user).data,
            "token":token
            })

    @action(detail=False,methods=['post'])
    def signup(self,request):
        """Handle HTTP POST request."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UsersSerializer(user).data
        return Response(data)
        
    @action(detail=False,methods=['post'])
    def verified(self,request):
        serializer= UserVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message":"congratulations!!!"},status=status.HTTP_200_OK)