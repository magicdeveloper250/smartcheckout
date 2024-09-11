import threading
import random
from .app import App


class AppList:
    def __init__(self) -> None:
        self.list = {}
        self.lock = threading.RLock()

    def add(self, app) -> None:
        self.lock.acquire()
        if not self.list.get(app.id):
            self.list[app.id] = app
        self.lock.release()

    def remove(self, app) -> bool:
        self.lock.acquire()
        try:
            del self.list[app.id]
        except KeyError:
            return False
        finally:
            self.lock.release()

    def get(self, id) -> App:
        return self.list.get(id)

    def get_random(self):
        return random.choice(self.list)

    def to_list(self) -> list[dict]:
        return [app.to_dict() for app in self.list.values()]
