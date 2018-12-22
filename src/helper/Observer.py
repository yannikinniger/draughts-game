import abc


class Observer:

    @abc.abstractmethod
    def update_(self, subject):
        pass


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        observer.subject = self
        self._observers.append(observer)

    def detach(self, observer):
        observer._subject = None
        self._observers.remove(observer)

    def _notify(self):
        for observer in self._observers:
            observer.update_(self)
