class Queue:
    def __init__(self):
        self._patients = []

    def add(self, patient):
        self._patients.append(patient)

    def remove(self):
        if self._patients:
            return self._patients.pop(0)
        else:
            return None

    def get_next_patient(self):
        return self._patients[0] if self._patients else None
