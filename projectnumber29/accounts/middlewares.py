from .models import User,Profile
from django.http import HttpRequest

class requestMidlleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,requset:HttpRequest):
        try:
            username=requset.user.get_username()
        except User.DoesNotExist:
            pass


        try:
            profile=Profile.objects.get(user__username=username)
            requset.profile=profile
        except Profile.DoesNotExist:
            pass

        response=self.get_response(requset)

        return response