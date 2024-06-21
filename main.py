import cmath
import random

class Qubit:
    def __init__(self, a, b):
        norm = cmath.sqrt(abs(a)**2 + abs(b)**2)
        self.a = a / norm
        self.b = b / norm

    def measure(self):
        probability_false = abs(self.a)**2
        if random.random() < probability_false:
            self.a, self.b = 1, 0
            return [1, 0]  # Estado |0>
        else:
            self.a, self.b = 0, 1
            return [0, 1]  # Estado |1>
    
    def hadamard(self):
        a_new = (self.a + self.b) / cmath.sqrt(2)
        b_new = (self.a - self.b) / cmath.sqrt(2)
        self.a, self.b = a_new, b_new
        
    def cnot(self, target):
        if self.measure() == [0, 1]:  
            target.a, target.b = target.b, target.a
            
    def pauli_x(self):
        self.a, self.b = self.b, self.a

    def pauli_z(self):
        self.b *= -1

def create_bell_pair():
    q1 = Qubit(1, 0)
    q2 = Qubit(1, 0)  
    q1.hadamard()
    q1.cnot(q2)
    return q1, q2

def teleport(q_input, q_bell1, q_bell2):
    q_input.cnot(q_bell1)
    q_input.hadamard()
    
    print(f'Estado do qubit de entrada: {q_input.a} e {q_input.b}')
    
    print(f'Estado do qubit de Bell 1: {q_bell1.a} e {q_bell1.b}')
    print(f'Estado do qubit de Bell 2: {q_bell2.a} e {q_bell2.b}')
    
    # Medições
    m1 = q_input.measure()
    m2 = q_bell1.measure()
    
    print(f'Medições: {m1} e {m2}')

    if m1 == [1, 0] and m2 == [0, 1]:
        q_bell2.pauli_x()
    elif m1 == [0, 1] and m2 == [1, 0]:
        q_bell2.pauli_z()
    elif m1 == [0, 1] and m2 == [0, 1]:
        q_bell2.pauli_x()
        q_bell2.pauli_z()

def main():
    q_input = Qubit(1, 0)  
    q_bell1, q_bell2 = create_bell_pair()
    original_state = q_input.measure()
    print(f'O estado original: {original_state}')
    teleport(q_input, q_bell1, q_bell2)
    teleported_state = q_bell2.measure()
    print(f'O estado teletransportado: {teleported_state}')

if __name__ == '__main__':
    main()