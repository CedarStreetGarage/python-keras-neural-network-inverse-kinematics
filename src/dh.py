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

    def transform_summary(self):
        print('\n\nHomogeneous transformation:')
        pprint(self.c)

    def jacobian(self):
        t = self.c * self.o
        m = Matrix(t[:3])
        b = Matrix(['theta1', 'theta2', 'theta3'])
        j = m.jacobian(b)
        return simplify(j)

    def eigen(self):
        j = self.jacobian()
        e = Matrix([j.eigenvals()])
        return simplify(e)

    def determinant(self):
        j = self.jacobian()
        d = Matrix([j.det()])
        return simplify(d)

    def eval_determinant(self, params):
        d = self.determinant()
        r = d.evalf(subs=params)
        return r[0]

    def jacobian_summary(self):
        print('\n\nTranslation Jacobian:')
        pprint(self.jacobian())

    def determinant_summary(self):
        print('\n\nTranslation Jacobian determinant:')
        pprint(self.determinant())

    def eigenvalue_summary(self):
        print('\n\nTranslation Jacobian eigenvalues:')
        pprint(self.eigen())

