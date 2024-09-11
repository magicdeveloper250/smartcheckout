import uuid
import threading


class Product:
    def __init__(self, **kwargs) -> None:

        self.id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.category = kwargs.get("category")
        self.quality = kwargs.get("quality")
        self.unit = kwargs.get("unit")
        self.quantity = kwargs.get("quantity")
        self.price = kwargs.get("price")
        self.link = kwargs.get("link")
        self.more = kwargs.get("more")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "quality": self.quality,
            "unit": self.unit,
            "quantity": self.quantity,
            "price": self.price,
            "link": self.link,
            "more": self.more,
        }

    def __getitem__(self, key):
        return getattr(self, key, None)

    def __str__(self) -> str:
        return f"{self.name} {self.category} {self.quality} {self.unit} {self.price} {self.link} {self.more} "


class CartNode:
    def __init__(self, name) -> None:
        self.id = uuid.uuid4()
        self.start_at = None
        self.end_at = None
        self.products = set()
        self.lock = threading.RLock()
        self.name = name

    def add(self, product: Product) -> Product:
        self.lock.acquire()
        self.products.add(product)
        self.lock.release()
        return product

    def get(self, product_id: str) -> Product:
        products_iter = iter(self.products)
        result = None
        while True:
            try:
                p: Product = next(products_iter)
                if p.id == product_id:
                    result = p
                    break
            except StopIteration:
                break
        return result

    def update(self, new_product: Product) -> bool:
        p = self.get(new_product.id)
        try:
            self.lock.acquire()
            self.products.remove(p)
            self.products.add(new_product)
            self.lock.release()
            return True
        except KeyError:
            return False

    def remove(self, product_id: str) -> bool:
        try:
            self.lock.acquire()
            self.products.remove(self.get(product_id))
            self.lock.release()
            return True
        except KeyError:
            return False

    def get_qty(self) -> float:
        qty = 0
        for product in self.products:
            qty += product.qty

    def get_units(self) -> int:
        units = 0
        for product in self.products:
            units += product.unit
        return units

    def get_total_price(self) -> float:
        total = 0
        for product in self.products:
            total += product.price
        return total

    def get_length(self) -> int:
        return len(self.products)

    def to_dict(self) -> dict:
        return {
            "id": str(self.id),
            "name": self.name,
            "products": [product.to_dict() for product in self.products],
            "amount": f"{self.get_total_price():2f}",
        }

    def __str__(self) -> str:
        return f"id:{self.id}, products: {str(self.products)}"


class CartList:
    def __init__(self) -> None:
        self.carts: list = {}
        self.lock = threading.RLock()

    def add(self, cart_node: CartNode):
        self.lock.acquire()
        self.carts[str(cart_node.id)] = cart_node
        self.lock.release()
        return True

    def remove(self, cartId):
        try:
            self.lock.acquire()
            del self.carts[cartId]
            self.lock.release()
        except KeyError:
            return False
        return True

    def getCart(self, cartId):
        try:
            return self.carts[cartId]
        except KeyError:
            return False

    def updateCart(self, new_cart: CartNode):
        try:
            self.lock.acquire()
            self.carts[new_cart.id] = new_cart
            self.lock.release()
        except KeyError:
            return 1

    def __str__(self):
        return str(self.carts)


def test():
    p = Product(
        name="sugar",
        category="Food",
        quality="Best",
        unit="Number",
        price=5000.0,
        quantity=3,
    )
    cart = CartNode()
    cart.add(p)
    cart.add(p)
    cartList = CartList()
    cartList.add(cart)
    print(cartList)


if __name__ == "__main__":
    test()
