from apps.account.application import user

class UserView(user.User):
    def list(self, request, *args, **kwargs):
        return self.list_user(request, *args, **kwargs)
