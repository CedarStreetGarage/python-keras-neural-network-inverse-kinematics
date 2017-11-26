from sympy          import simplify, pprint
from sympy.matrices import Matrix
from homogeneous    import Homogeneous


class DH(object):

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

    def summary(self):
        print('\nAggregate transformation:')
        pprint(self.c)
        print('\nTranslation component:')
        trans = self.c * self.o
        pprint(Matrix(trans[:3]))
        print('\nTranslation Jacobian:')

