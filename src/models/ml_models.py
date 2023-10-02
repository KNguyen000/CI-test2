

class Model:
    def __init__(self, name, accuracy, f1):
        self.name = name
        self.accuracy = accuracy
        self.f1 = f1

    def __str__(self):
        return f"{self.name} has acc: {self.accuracy}, f1:{self.f1}"


def give_accuracy(s: Model) -> str:
    return s.accuracy