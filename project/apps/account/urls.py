from django.urls import path

from apps.account.views import AccountView, LoginView, LogoutView, RefreshView

app_name = 'account'

urlpatterns = [
    # Create/Delete user account.
    path('create-account', AccountView.as_view({'post': 'create'}), name='create-account'),
    path('delete-account/<int:pk>', AccountView.as_view({'delete': 'destroy'}), name='delete-account'),

    # User Login/Logout using JWT.
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),

    # Refresh JWT.
    path('refresh', RefreshView.as_view(), name='refresh'),
]
