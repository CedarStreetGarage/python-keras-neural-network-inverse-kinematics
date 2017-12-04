from sympy           import solve, symbols
from sympy.matrices  import Matrix
from sympy.functions import re
from src.chain       import Chain


TARGET = [1.0, 0.75, 1.0]


class IK(object):

    def ik(self):
        chain = Chain().make()
        chain.transform_summary()

        theta1, theta2, theta3 = symbols('theta1:4')

        f = chain.c * Matrix([0, 0, 0, 1])
        f = Matrix(f[:3])

        solutions = solve(f - Matrix(TARGET), (theta1, theta2, theta3))

        print('\n\nTarget:')
        print(TARGET)

        print('\n\nSolutions:')
        for sol in solutions:
            t1 = re(sol[0])
            t2 = re(sol[1])
            t3 = re(sol[2])
            print('IK Angles: ' + str([t1, t2, t3]))
            r = chain.forward({
                'theta1': t1,
                'theta2': t2,
                'theta3': t3
            })
            print('FK Points: ' + str(r))
            print('')

