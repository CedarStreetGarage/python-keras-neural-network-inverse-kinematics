from sympy import symbols, pi
from dh    import DH


class Chain(object):

    def make(self):
        dh = DH()
        a1, a2, a3 = symbols('a1:4')
        dh.link(1.0, a1, 0.0, 0.0)
        dh.link(1.0, a2, 0.2, pi/2)
        dh.link(1.0, a3, 0.1, 0.0)
        return dh

