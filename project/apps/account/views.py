from apps.account.application import sign


class AccountView(sign.Account):
    """Account View.

    View for user account creation and deletion.
    """
    def create(self, request, *args, **kwargs):
        return self.create_account(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return self.delete_account(request, *args, **kwargs)


class LoginView(sign.Login):
    """Login View.

    View for user login using JWT.
    """
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class LogoutView(sign.Logout):
    """Logout View.

    View for user logout by blacklisting the refresh token.
    """
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class RefreshView(sign.Refresh):
    """Refresh View.

    View for refreshing access and refresh tokens.
    """
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
