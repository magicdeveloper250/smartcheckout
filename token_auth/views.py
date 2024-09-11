from urllib import response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import CookieTokenRefreshSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status


class MyTokenObtainPairView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data["refresh"]
        response.set_cookie("refresh_token", token, httponly=True)
        return response


class BlacklistRefreshView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        token = (
            request.COOKIES.get("refresh_token")
            if request.COOKIES.get("refresh_token")
            else request.data.get("refresh_token")
        )
        if token:
            refresh_token = RefreshToken(token)
            refresh_token.blacklist()
            response = Response("Success")
            response.delete_cookie("refresh_token")
            return response
        return Response(
            {"success": False, "error": "No refresh token provided"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class CookieTokenObtainPairView(TokenObtainPairView):
    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get("refresh"):
            cookie_max_age = 3600 * 24 * 14  # 14 days
            response.set_cookie(
                "refresh_token",
                response.data["refresh"],
                max_age=cookie_max_age,
                httponly=True,
            )
            del response.data["refresh"]
        return super().finalize_response(request, response, *args, **kwargs)


class CookieTokenRefreshView(TokenRefreshView):
    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get("refresh"):
            cookie_max_age = 3600 * 24 * 14  # 14 days
            response.set_cookie(
                "refresh_token",
                response.data["refresh"],
                max_age=cookie_max_age,
                httponly=True,
                samesite=None,
                secure=True,
            )
            del response.data["refresh"]
        return super().finalize_response(request, response, *args, **kwargs)

    serializer_class = CookieTokenRefreshSerializer
