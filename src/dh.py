from sympy          import simplify, pprint
from sympy.matrices import Matrix
from homogeneous    import Homogeneous


class DH(object):

    def __init__(self):
        self.h = Homogeneous()
        self.o = self.h.origin()
        self.c = self.h.stationary()

    def link(self, d, theta, a, alpha):
        tz = self.h.translate_z(d)
        rz = self.h.rotate_z(theta)
        tx = self.h.translate_x(a)
        rx = self.h.rotate_x(alpha)
        self.c = simplify(self.c * tz * rz * tx * rx)

    def forward(self, params):
        r = self.c.evalf(subs=params) * self.o
        return r[:3]

    def transform(self):
        print('\n\nHomogeneous transformation:\n')
        pprint(self.c)

    def determinant(self):
        t = self.c * self.o
        m = Matrix(t[:3])
        b = Matrix(['theta1', 'theta2', 'theta3'])
        j = m.jacobian(b)
        d = Matrix([j.det()])
        print('\n\nTranslation Jacobian determinant:\n')
        pprint(simplify(d))

