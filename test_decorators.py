import unittest
from queues.queue import Queue
from decorators.priority_decorator import PriorityDecorator
from decorators.addon_decorator import AddonDecorator
from queues.patient import Patient

class TestDecoratorSuccess(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()
        self.priority_queue = PriorityDecorator(self.queue)
        self.addon_queue = AddonDecorator(self.priority_queue)

    def test_priority_decorator_success(self):
        for i in range(10):
            patient = Patient(f"Patient{i}")
            self.priority_queue.add(patient)

        # Test whether the first patient in priority queue is Patient0
        next_patient = self.priority_queue.get_next_patient()
        self.assertEqual(next_patient.get_name(), "Patient0")

        # Test whether the second patient in priority queue is Patient1
        next_patient = self.priority_queue.get_next_patient()
        self.assertEqual(next_patient.get_name(), "Patient1")
    
    def test_addon_decorator_success(self):
        for i in range(10):
            patient = Patient(f"Patient{i}")
