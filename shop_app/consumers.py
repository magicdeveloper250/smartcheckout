from api import serializers
from api.models import App
from api.models import User
from channels.generic.websocket import WebsocketConsumer
from security.functions import quantities_are_equal, prices_are_equal, units_are_equal
from utils.app import App as MemoryApp
from utils.app_list import AppList
from utils.cart_list import Product
from asgiref.sync import async_to_sync
import json
from api.serializers import UserSerializer

apps = AppList()


class CartConsumer(WebsocketConsumer):

    def connect(self):
        async_to_sync(self.channel_layer.group_add)("cart", self.channel_name)
        self.accept()

    def disconnect(self, code):
        pass

    def chat_message(self, event):
        self.send(text_data=json.dumps(event["data"]))

    def receive(self, text_data):
        text_json = json.loads(text_data)
        # Check if it is a valid request
        if text_json.get("action"):
            app_id = text_json.get("app_id")
            action = text_json.get("action")
            app = apps.get(app_id)
            if action == "all":

                self.send(
                    json.dumps(
                        {
                            "receiver": str(self.channel_name),
                            "type": "all",
                            "status": "success",
                            "message": "all apps and their carts",
                            "apps": apps.to_list(),
                        }
                    )
                )

            elif action == "add":
                if app:
                    product_json = text_json.get("data", {}).get("product")
                    product = Product(
                        id=product_json.get("id"),
                        name=product_json.get("name"),
                        category=product_json.get("category"),
                        quality=product_json.get("quality"),
                        unit=product_json.get("unit"),
                        price=product_json.get("price"),
                        quantity=product_json.get("quantity"),
                    )
                    app.cart.add(product)
                    async_to_sync(self.channel_layer.group_send)(
                        "cart",
                        {
                            "type": "chat_message",
                            "data": {
                                "receiver": "all",
                                "status": "success",
                                "type": "cart",
                                "message": "new product added",
                                "cart": app.cart.to_dict(),
                            },
                        },
                    )
                else:
                    self.send(
                        json.dumps(
                            {
                                "receiver": app_id,
                                "status": "failed",
                                "message": "app not found",
                            }
                        )
                    )

            elif action == "remove":
                if app:
                    app.cart.remove(text_json.get("data", {}).get("product").get("id"))
                    async_to_sync(self.channel_layer.group_send)(
                        "cart",
                        {
                            "type": "chat_message",
                            "data": {
                                "receiver": "all",
                                "status": "success",
                                "type": "remove",
                                "message": "product removed",
                                "cart": app.cart.to_dict(),
                            },
                        },
                    )
                else:
                    self.send(
                        json.dumps(
                            {
                                "receiver": app_id,
                                "status": "failed",
                                "message": "app not found",
                            }
                        )
                    )

            elif action == "update":
                if app:
                    product_json = text_json.get("data", {}).get("product")
                    product = Product(
                        id=product_json.get("id"),
                        name=product_json.get("name"),
                        category=product_json.get("category"),
                        quality=product_json.get("quality"),
                        unit=product_json.get("unit"),
                        price=product_json.get("price"),
                        quantity=product_json.get("quantity"),
                    )
                    app.cart.update(product)
                    async_to_sync(self.channel_layer.group_send)(
                        "cart",
                        {
                            "type": "chat_message",
                            "data": {
                                "receiver": "all",
                                "status": "success",
                                "type": "update",
                                "message": "product updated",
                                "cart": app.cart.to_dict(),
                            },
                        },
                    )
                else:
                    self.send(
                        json.dumps(
                            {
                                "receiver": app_id,
                                "status": "failed",
                                "message": "app not found",
                            }
                        )
                    )

            elif action == "get":
                if app:
                    product = app.cart.get(
                        text_json.get("data", {}).get("product").get("id")
                    )
                    print(product)
                    if product:
                        self.send(
                            json.dumps(
                                {
                                    "receiver": app_id,
                                    "status": "success",
                                    "data": product.to_dict(),
                                }
                            )
                        )
                    else:
                        self.send(
                            json.dumps(
                                {
                                    "receiver": app_id,
                                    "status": "failed",
                                    "data": "product not found",
                                }
                            )
                        )
                else:
                    self.send(
                        json.dumps(
                            {
                                "receiver": app_id,
                                "status": "failed",
                                "message": "app not found",
                            }
                        )
                    )

            else:
                self.send(
                    json.dumps(
                        {
                            "receiver": app_id,
                            "status": "failed",
                            "message": "unknown action",
                        }
                    )
                )
        else:
            self.send(
                json.dumps(
                    {
                        "receiver": text_json.get("app_id"),
                        "status": "failed",
                        "message": "bad request",
                    }
                )
            )


class AppConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, code):
        pass

    def receive(self, text_data):
        text_json = json.loads(text_data)
        # Check if it is a valid request
        if text_json.get("id") and text_json.get("action"):
            app_id = text_json.get("id")
            action = text_json.get("action")

            if action == "connect":
                try:
                    app = App.objects.get(id=app_id)
                    app.status = "online"
                    app.save()
                    cust = User.objects.get(id=app.cust_id.id)
                    serializer = UserSerializer(cust)
                    memory_app = MemoryApp(app_id, serializer.data.get("name"))
                    apps.add(memory_app)
                    self.send(
                        json.dumps(
                            {"receiver": app_id, "status": "success", "token": ""}
                        )
                    )
                except App.DoesNotExist:
                    self.send(
                        json.dumps(
                            {
                                "receiver": app_id,
                                "status": "failed",
                                "message": "app id doesn't exist",
                            }
                        )
                    )

            elif action == "disconnect":
                try:

                    app = App.objects.get(id=app_id)
                    app.status = "offline"
                    app.save()
                    apps.remove(app)
                    self.send(json.dumps({"receiver": app_id, "status": "success"}))
                except (App.DoesNotExist, KeyError):
                    self.send(
                        json.dumps(
                            {
                                "receiver": app_id,
                                "status": "failed",
                                "message": "app does not exist",
                            }
                        )
                    )

            elif action == "verify":
                receipt_qty = text_json.get("receipt_qty")
                receipt_amount = text_json.get("receipt_amount")
                receipt_unit = text_json.get("receipt_unit")
                weight_detector_qty = text_json.get("detector_qty")
                app_cart = apps.get(app_id).cart
                app_qty = app_cart.get_qty()
                app_units = app_cart.get_units()
                app_amount = app_cart.get_total_price()

                passed = all(
                    [
                        quantities_are_equal(
                            [receipt_qty, app_qty, weight_detector_qty]
                        ),
                        units_are_equal([receipt_unit, app_units]),
                        prices_are_equal([receipt_amount, app_amount]),
                    ]
                )
                if passed:
                    self.send(json.dumps({"receiver": app_id, "status": "success"}))
                else:
                    # Send signal to the alarm
                    pass

            else:
                self.send(
                    json.dumps(
                        {
                            "receiver": app_id,
                            "status": "failed",
                            "message": "unknown action",
                        }
                    )
                )
        else:
            self.send(
                json.dumps(
                    {
                        "receiver": text_json.get("id"),
                        "status": "failed",
                        "message": "bad request",
                    }
                )
            )
