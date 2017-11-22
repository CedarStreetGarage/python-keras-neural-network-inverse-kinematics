import numpy as np
from model import Model
from scale import Scale


model = Model().make()
model.load_weights('model_weights.h5')

angle_scale    = Scale([-np.pi/4, np.pi/4], [-0.5, 0.5])
position_scale = Scale([-10.0,    10.0   ], [-0.5, 0.5])

p0 = position_scale.forward_scale(2.0)
p1 = position_scale.forward_scale(1.0)
p2 = position_scale.forward_scale(1.5)

d = np.array([[p0, p1, p2]])
r = model.predict(d)

a0 = angle_scale.reverse_scale(r[0][0])
a1 = angle_scale.reverse_scale(r[0][1])
a2 = angle_scale.reverse_scale(r[0][2])
print([a0, a1, a2])

