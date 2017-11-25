import numpy as np
from scale import Scale
from chain import Chain


class Generator(object):

    def __init__(self):
        self.chain = Chain().make()
        self.angle_scale    = Scale([-np.pi/4, np.pi/4], [-0.5, 0.5])
        self.position_scale = Scale([-10.0,    10.0   ], [-0.5, 0.5])

    def generate_angles(self):
        a1 = np.random.uniform(-np.pi/4, np.pi/4)
        a2 = np.random.uniform(-np.pi/4, np.pi/4)
        a3 = np.random.uniform(-np.pi/4, np.pi/4)
        a1 = self.angle_scale.forward_scale(a1)
        a2 = self.angle_scale.forward_scale(a2)
        a3 = self.angle_scale.forward_scale(a3)
        return [a1, a2, a3]

    def generate_positions(self, angles):
        p = self.chain.forward({
            'a1': angles[0], 
            'a2': angles[1], 
            'a3': angles[2]
        })
        p0 = self.position_scale.forward_scale(p[0])
        p1 = self.position_scale.forward_scale(p[1])
        p2 = self.position_scale.forward_scale(p[2])
        return [p0, p1, p2]

    def make(self, batch_size):
        while 1:
            features = []
            labels   = []
            for i in range(batch_size):
                angles    = self.generate_angles()
                positions = self.generate_positions(angles)
                features.append(positions)
                labels.append(angles)
            yield np.array([features, labels])


