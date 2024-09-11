from .cart_list import CartNode
from typing import Any


class App:
    def __init__(self, id, name) -> None:
        self.cart = CartNode(name)
        self.id = id

    def to_dict(self) -> dict[str, Any]:
        return {"id": self.id, "cart": self.cart.to_dict()}
