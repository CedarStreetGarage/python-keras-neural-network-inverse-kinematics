import numpy as np
from sympy import symbols, pi
from flow  import Flow
from model import Model
from chain import Chain
from scale import Scale


Flow().defaults()

model = Model().make()
model.load_weights('model_weights.h5')

chain = Chain().make()

angle_scale    = Scale([-np.pi/4, np.pi/4], [-0.5, 0.5])
position_scale = Scale([-10.0,    10.0   ], [-0.5, 0.5])

# Position
px = 2.0
py = 1.0
pz = 1.5
print([px, py, pz])

# Normalize the position
p1 = position_scale.forward_scale(px)
p2 = position_scale.forward_scale(py)
p3 = position_scale.forward_scale(pz)
p  = np.array([[p1, p2, p3]])

# Inference returns normalized angle
r = model.predict(p)

# Inference de-normalized angled
theta1 = angle_scale.reverse_scale(r[0][0])
theta2 = angle_scale.reverse_scale(r[0][1])
theta3 = angle_scale.reverse_scale(r[0][2])
#print([theta1, theta2, theta3])

# Compute position with real transform based on angle
q = chain.forward({
    'theta1': theta1, 
    'theta2': theta2, 
    'theta3': theta3
})

# q should be non-normalized positions
print(q)


