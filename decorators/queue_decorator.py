from abc import ABC, abstractmethod

class QueueDecorator(ABC):
    def __init__(self, queue):
        self.queue = queue

    @abstractmethod
    def add(self, patient):
        pass

    @abstractmethod
    def remove(self, patient):
        pass

    @abstractmethod
    def get_next_patient(self):
        pass
