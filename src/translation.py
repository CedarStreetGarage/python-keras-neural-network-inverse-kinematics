from sympy.matrices import Matrix


class Translation(object):

    def stationary(self):
        return Matrix([0, 0, 0])

    def translate_x(self, x):
        return Matrix([x, 0, 0])

    def translate_y(self, y):
        return Matrix([0, y, 0])

    def translate_z(self, z):
        return Matrix([0, 0, z])

