from decorators.queue_decorator import QueueDecorator

class AddonDecorator(QueueDecorator):
    def __init__(self, queue):
        super().__init__(queue)
        self.addon_queue = []

    def add(self, patient):
        self.addon_queue.append(patient)

    def remove(self, patient):
        self.addon_queue.remove(patient)

    def get_next_patient(self):
        if self.addon_queue:
            return self.addon_queue.pop(0)
        else:
            return self.queue.get_next_patient()
