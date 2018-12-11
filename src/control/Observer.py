import abc


class Observer:

    def __init__(self):
        self._subject = None

    @abc.abstractmethod
    def update(self):
        pass


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        observer._subject = self
        self._observers.append(observer)

    def detach(self, observer):
        observer._subject = None
        self._observers.remove(observer)

    def _notify(self):
        for observer in self._observers:
            observer.update()
