import abc


class Subscriber:

    @abc.abstractmethod
    def update(self):
        pass


class Publisher:
    def __init__(self):
        self.subscribers = set()

    def register(self, who):
        self.subscribers.add(who)

    def unregister(self, who):
        self.subscribers.discard(who)

    def dispatch(self):
        for subscriber in self.subscribers:
            subscriber.update()
