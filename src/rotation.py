from sympy import sin, cos
from sympy.matrices import Matrix


class Rotation(object):

    def stationary(self):
        return Matrix([
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0]
        ])

    def rotate_x(self, x):
        return Matrix([
            [1.0, 0.0,     0.0   ],
            [0.0, cos(x), -sin(x)],
            [0.0, sin(x),  cos(x)]
        ])

    def rotate_y(self, y):
        return Matrix([
            [ cos(y), 0.0, sin(y)],
            [ 0.0,    1.0, 0.0   ],
            [-sin(y), 0.0, cos(y)]
        ])

    def rotate_z(self, z):
        return Matrix([
            [cos(z), -sin(z), 0.0],
            [sin(z),  cos(z), 0.0],
            [ 0.0,    0.0,    1.0]
        ])

