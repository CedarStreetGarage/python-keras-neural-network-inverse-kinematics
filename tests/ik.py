from sympy           import solve, symbols
from sympy.matrices  import Matrix
from sympy.functions import re
from src.chain       import Chain


TARGET = [1.0, 0.5, 1.0]


class IK(object):

    def ik(self):
        chain = Chain().make()
        chain.transform_summary()

        theta1, theta2, theta3 = symbols('theta1:4')

        f = chain.c * Matrix([0, 0, 0, 1])
        f = Matrix(f[:3])

        s = solve(f - Matrix(TARGET), (theta1, theta2, theta3))

        print('\n\nTarget:')
        print(TARGET)

        print('\n\nSolutions:')
        for i in s:
            print('IK Angles: ' + str(i))
            r = chain.forward({
                'theta1': re(i[0]),
                'theta2': re(i[1]),
                'theta3': re(i[2])
            })
            print('FK Points: ' + str(r))
            print('')

