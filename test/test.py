from sympy  import symbols
from src.dh import DH


class Test(object):

    def test(self):
        dh_chain = DH()
        a1, theta1 = symbols('a1 theta1')
        a2, theta2 = symbols('a2 theta2')

        # link(d, theta, a, alpha)
        dh_chain.link(0, theta1, a1, 0)
        dh_chain.link(0, theta2, a2, 0)

        print('TWO LINK PLANAR TEST')
        print('--------------------')
        dh_chain.transform_summary()


