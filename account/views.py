from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .renderers import UserRenderer
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import *
from rest_framework import generics
from .filters import *
from django_filters import rest_framework as filters


"""
Api for authenticate users
"""
class LoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                user_serializer = UserSerializer(user)
                return Response({"user": user_serializer.data, "message": "User Login is Successfully!", 'status': 200},
                                status=status.HTTP_200_OK)
            else:
                return Response({"message": "User credentials are incorrect!", 'status': 400},
                                status=status.HTTP_400_BAD_REQUEST)


"""
Api for create user
"""
class UserCreateView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"user": serializer.data, "message": "User Registered Successfully!", 'status': 201},
                            status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"errors": serializer.errors, "message": "User is not Registered Successfully!", 'status': 400},
                status=status.HTTP_400_BAD_REQUEST)


"""
Api for update user
"""
class UserUpdateView(APIView):
    renderer_classes = [UserRenderer]

    def get_object(self, uid):
        try:
            return User.objects.get(id=uid)
        except User.DoesNotExist:
            return Response(
                {"message": "User is not Found", 'status': 404},
                status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        uid = request.GET.get('uid') # get user id from url parameter
        instance = self.get_object(uid)
        serializer = EditUserSerializer(instance=instance, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"user": serializer.data, "message": "User updated Successfully!", 'status': 204},
                            status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {"errors": serializer.errors, "message": "User is not updated Successfully!", 'status': 400},
                status=status.HTTP_400_BAD_REQUEST)


"""
Api for getting single or list of users
"""
class UserView(APIView):
    renderer_classes = [UserRenderer]

    def get_object(self, uid):
        try:
            return User.objects.get(id=uid)
        except User.DoesNotExist:
            return Response(
                {"message": "User is not Found", 'status': 404},
                status=status.HTTP_404_NOT_FOUND)

    def get(self, request, *args, **kwargs):
        user = None
        serializer = None
        uid = request.GET.get('uid') # get user id from url parameter
        if uid is not None:
            user = self.get_object(uid)
            serializer = UserSerializer(user, many=False)
        else:
            user = User.objects.all()
            serializer = UserSerializer(user, many=True)

        return Response({"user": serializer.data, 'status': 200},
                            status=status.HTTP_200_OK)


"""
Api for searching or filtering users
"""
class UserSearchView(generics.ListAPIView):
    renderer_classes = [UserRenderer]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserFilter