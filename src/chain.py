from homogeneous import Homogeneous
from sympy import simplify


class Chain(object):

    def __init__(self):
        self.h = Homogeneous()
        self.o = self.h.origin()
        self.c = self.h.stationary()

    def link(self, d, theta, r, alpha):
        tz = self.h.translate_z(d)
        rz = self.h.rotate_z(theta)
        tx = self.h.translate_x(r)
        rx = self.h.rotate_x(alpha)
        self.c = simplify(self.c * tz * rz * tx * rx)

    def forward(self, params):
       r = self.c.evalf(subs=params) * self.o
       return r[:3]

    def reverse(self, mat):
        b = self.c * mat
        s = self.c.LUsolve(b)
        return s

