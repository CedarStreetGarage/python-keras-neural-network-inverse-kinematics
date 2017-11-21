from rotation import Rotation
from translation import Translation
from sympy.matrices import Matrix


class Homogeneous(object):

    def __init__(self):
        self.r = Rotation()
        self.t = Translation()

    def origin(self):
        return Matrix([0.0, 0.0, 0.0, 1.0])

    def stationary(self):
        return Matrix([
            [1.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0]
        ])

    def _build(self, r, t):
        return r.col_insert(3, t).row_insert(3, self.origin().T)

    def translate_x(self, x):
        r = self.r.stationary()
        t = self.t.translate_x(x)
        return self._build(r, t)

    def translate_y(self, y):
        r = self.r.stationary()
        t = self.t.translate_y(y)
        return self._build(r, t)

    def translate_z(self, z):
        r = self.r.stationary()
        t = self.t.translate_z(z)
        return self._build(r, t)

    def rotate_x(self, x):
        r = self.r.rotate_x(x)
        t = self.t.stationary()
        return self._build(r, t)

    def rotate_y(self, y):
        r = self.r.rotate_y(y)
        t = self.t.stationary()
        return self._build(r, t)

    def rotate_z(self, z):
        r = self.r.rotate_z(z)
        t = self.t.stationary()
        return self._build(r, t)
 
