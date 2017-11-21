import numpy as np
from sympy import symbols, pi
from chain import Chain


class Generator(object):

    def __init__(self):
        self.set_chain()

    def set_chain(self):
        self.chain = Chain()
        a1, a2, a3 = symbols('a1:4')
        self.chain.link(1.0, a1, 0.0, 0.0)
        self.chain.link(1.0, a2, 0.2, pi/2)
        self.chain.link(1.0, a3, 0.1, 0.0)

    def generate_angles(self):
        a1 = np.random.uniform(0.0, np.pi/4)
        a2 = np.random.uniform(0.0, np.pi/4)
        a3 = np.random.uniform(0.0, np.pi/4)
        return a1, a2, a3

    def generate_positions(self, angles):
        p = self.chain.forward({a1:angles[0], a2:angles[1], a3:angles[2]})
        return p[0], p[1], p[2]

    def make(self, batch_size):
        while 1:
            features = []
            labels   = []
            for i in range(batch_size):
                f = self.generate_angles()
                l = self.generate_positions(f)
                features.append(f)
                labels.append(l)
            yield features, labels


