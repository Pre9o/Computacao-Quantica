import cmath
from collections import defaultdict

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
    
    def hadamard(self):
        a = self.a
        b = self.b
        self.a = (a + b) / cmath.sqrt(2)
        self.b = (a - b) / cmath.sqrt(2)


class Basis:
    def __init__(self, basis):
        self.basis = basis

    def __str__(self):
        return ', '.join(str(b) for b in self.basis)

class QV:
    def __init__(self, mapping):
        self.mapping = defaultdict(complex, mapping)

    def __str__(self):
        return ', '.join(f'{k}: {v}' for k, v in self.mapping.items())

def qv(pairs):
    return QV(dict(pairs))

# Exemplo de uso
qFalse = QV({Qubit(1, 0): 1})
qTrue = QV({Qubit(0, 1): 1})
qFT = qv([(Qubit(1, 0), 1/cmath.sqrt(2)), (Qubit(0, 1), 1/cmath.sqrt(2))])

print(qFalse)
print(qTrue)
print(qFT)


qubit = Qubit(cmath.sqrt(0.5), cmath.sqrt(0.5))
print(qubit)
print("Measurement:", qubit.measure())

qubit.hadamard()
print(qubit)

basis = Basis([Qubit(1, 0), Qubit(0, 1)])
print(basis)

mapping = qv([(Qubit(1, 0), 0.5), (Qubit(0, 1), 0.5)])
print(mapping)