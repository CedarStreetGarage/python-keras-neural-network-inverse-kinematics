from src.chain import Chain
from sympy import symbols, pi, pprint

c = Chain()
q1, q2, q3 = symbols('q1:4')

c.link(1.0, q1, 0.0, 0.0)
c.link(1.0, q2, 0.2, pi/2)
c.link(1.0, q3, 0.1, 0.0)

r = c.forward({
    q1: 0.2,
    q2: 0.3,
    q3: 0.4
})
pprint(r)

#s = c.reverse(r)
#print(s)

