from django.urls import path

from apps.account.views import UserView

app_name = 'account'

urlpatterns = [
    path('user', UserView.as_view({'get': 'list'}), name='user-list'),
]