from decorators.queue_decorator import QueueDecorator

class PriorityDecorator(QueueDecorator):
    def __init__(self, queue):
        super().__init__(queue)
        self.priority_queue = []

    def add(self, patient):
        self.priority_queue.append(patient)

    def remove(self, patient):
        self.priority_queue.remove(patient)

    def get_next_patient(self):
        if self.priority_queue:
            return self.priority_queue.pop(0)
        else:
            return self.queue.get_next_patient()
