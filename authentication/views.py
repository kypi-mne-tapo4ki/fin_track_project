from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import RegistrationSerializer, UsersResponseSerializer


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        users = User.objects.all()
        serializer = UsersResponseSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        users = User.objects.all()
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

