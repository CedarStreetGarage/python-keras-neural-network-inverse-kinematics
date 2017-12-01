from src.chain import Chain


NUM_POINTS = 5


class Table(object):

    def table(self):
        chain = Chain().make()

        ts = [float(x-NUM_POINTS/2)/float(NUM_POINTS) for x in range(NUM_POINTS)]

        for t1 in ts:
            for t2 in ts:
                for t3 in ts:
                    d = chain.eval_determinant({'theta1': t1, 'theta2': t2, 'theta3': t3})
                    p = chain.forward({'theta1': t1, 'theta2': t2, 'theta3': t3})
                    print(t1, t2, t3, d, p)

