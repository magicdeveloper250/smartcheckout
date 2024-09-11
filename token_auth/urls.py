from .views import (
    CookieTokenRefreshView,
    MyTokenObtainPairView,
    BlacklistRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView
from django.urls import path

urlpatterns = [
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path(
        "token/refresh/",
        CookieTokenRefreshView.as_view(),
        name="token_refresh_pair",
    ),
    path("token/blacklist/", BlacklistRefreshView.as_view(), name="token_blacklist"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
