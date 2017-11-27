from sympy import symbols, pi
from dh    import DH


class Chain(object):

    def make(self):
        self.dh_chain = DH()
        theta1, theta2, theta3 = symbols('theta1:4')
        self.dh_chain.link(0, theta1, 1, 0)
        self.dh_chain.link(0, theta2, 1, pi/2)
        self.dh_chain.link(0, theta3, 1, 0)
        return self.dh_chain

