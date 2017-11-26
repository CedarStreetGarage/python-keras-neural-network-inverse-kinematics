from sympy import symbols, pi
from dh    import DH


class Chain(object):

    def make(self):
        self.dh_chain = DH()
        a1, a2, a3 = symbols('a1:4')
        self.dh_chain.link(1.0, a1, 0.0, 0.0)
        self.dh_chain.link(1.0, a2, 0.2, pi/2)
        self.dh_chain.link(1.0, a3, 0.1, 0.0)
        return self.dh_chain

