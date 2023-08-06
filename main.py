from queues.queue import Queue
from decorators.priority_decorator import PriorityDecorator
from decorators.addon_decorator import AddonDecorator
from queues.patient import Patient

def main():
    queue = Queue()

    priority_queue = PriorityDecorator(queue)
    addon_queue = AddonDecorator(priority_queue)

    # Adding patients to the queue
    patient1 = Patient("John")
    patient2 = Patient("Jane")
    patient3 = Patient("Smith")

    addon_queue.add(patient1)
    addon_queue.add(patient2)
    addon_queue.add(patient3)

    # Getting the next patient to be served
    next_patient = addon_queue.get_next_patient()
    print(f"Next patient to be served: {next_patient.get_name()}")  # Output: Next patient to be served: John

    # Remove the served patient from the queue
    served_patient = queue.remove()

    if served_patient:
        print(f"Served patient: {served_patient.get_name()}")  # Output: Served patient: John
    else:
        print("Queue is empty. No patients to be served.")

    # Getting the next patient after John
    next_patient = addon_queue.get_next_patient()
    if next_patient:
        print(f"Next patient to be served: {next_patient.get_name()}")  # Output: Next patient to be served: Jane
    else:
        print("Queue is empty. No patients to be served.")

if __name__ == "__main__":
    main()
