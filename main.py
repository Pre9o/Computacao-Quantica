import cmath

class Qubit:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a}|False> + {self.b}|True>'

    def measure(self):
        probability_false = abs(self.a)**2
        probability_true = abs(self.b)**2
        return 'False' if probability_false > probability_true else 'True'

class Basis:
    def __init__(self, basis):
        self.basis = basis

    def __str__(self):
        return ', '.join(str(b) for b in self.basis)

qubit = Qubit(cmath.sqrt(0.5), cmath.sqrt(0.5))
print(qubit)
print("Measurement:", qubit.measure())

basis = Basis([Qubit(1, 0), Qubit(0, 1)])
print(basis)