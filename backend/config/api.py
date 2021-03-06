from rest_framework import routers

from apps.users.views import UserViewSet
from apps.call_center.views import CustomerViewSet


# Settings
api = routers.DefaultRouter()
api.trailing_slash = '/?'

api.register(r'customers', CustomerViewSet)
api.register(r'users', UserViewSet)
