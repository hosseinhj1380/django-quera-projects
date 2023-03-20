from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import authentication,permissions,generics
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User


login = obtain_auth_token


class Logout(APIView):
    authentication_classes=[authentication.TokenAuthentication,]
    permission_classes=[permissions.IsAuthenticated,]

    def post(self,request):
        request.user.auth_token.delete()
        return Response(data={'message': f"Bye {request.user.username}!"},status=204)
    
    


class Register(generics.CreateAPIView):
    permission_classes=[permissions.AllowAny]
    serializer_class=UserSerializer
    queryset=User.objects.all()
    
    
    def post (self, request, *args, **kwargs):

        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
        created_obj=serializer.data
        data={'id':created_obj['id'], 'username':created_obj['username'],
        }

        return Response(data,status=201)