from django.contrib.auth.models import User
from .models import Profile


class EmailAuthBackend:
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExists:
            return None


#___для конвеера social auth___
def create_profile(backend, user, response, *args, **kwargs):
    Profile.objects.get_or_create(user=user)
    # print(11111111111111111111111)
    # print(response)
0