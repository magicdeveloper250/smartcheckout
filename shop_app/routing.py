from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("cart", consumers.CartConsumer.as_asgi()),
    path("app", consumers.AppConsumer.as_asgi()),
]
