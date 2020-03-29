from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
class ModifiedBackend(BaseBackend):

    def authenticate(self,request,username=None,password=None):
        if username is None or password is None:
            return None
        else:
            try:
                user = User.objects.get(username = username)
            except User.DoesNotExist:
                try:
                    user = User.objects.get(email = username)
                except User.DoesNotExist:
                    return None
            return user

    def get_user(self,user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

def authenticate(self,request,username=None,password=None):
    if username is None or password is None:
        return None
    else:
        try:
            user = User.objects.get(username = username)
        except User.DoesNotExist:
            try:
                user = User.objects.get(email = username)
            except User.DoesNotExist:
                return None
        return user