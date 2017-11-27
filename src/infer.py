import numpy as     np
from   flow  import Flow
from   model import Model
from   chain import Chain
from   scale import Scale


class Infer(object):

    def infer(self):
        Flow().defaults()

        model = Model().make()
        model.load_weights('model_weights.h5')

        chain = Chain().make()

        angle_scale    = Scale([-np.pi/4, np.pi/4], [-0.5, 0.5])
        position_scale = Scale([-10.0,    10.0   ], [-0.5, 0.5])

        # Reference angles
        theta1_ref =  0.4
        theta2_ref =  0.1
        theta3_ref =  0.25
        ref = np.array([theta1_ref, theta2_ref, theta3_ref])
        print('\nReference angles:')
        print(ref)

        # Forward kinematic positions
        px, py, pz = chain.forward({
            'theta1': theta1_ref, 
            'theta2': theta2_ref,
            'theta3': theta3_ref
        })
        print('\nComputed positions:')
        print(np.array([px, py, pz]))

        # Normalize the position
        px = position_scale.forward_scale(px)
        py = position_scale.forward_scale(py)
        pz = position_scale.forward_scale(pz)
        p  = np.array([[px, py, pz]])

        # Inference returns normalized angle
        r = model.predict(p)

        # De-normalized inference angles
        theta1_ik = angle_scale.reverse_scale(r[0][0])
        theta2_ik = angle_scale.reverse_scale(r[0][1])
        theta3_ik = angle_scale.reverse_scale(r[0][2])
        inf = np.array([theta1_ik, theta2_ik, theta3_ik])
        print('\nInferred IK angles:')
        print(inf)

        # Relative error
        err = np.abs(ref - inf) / ref
        print('\nAngle error (relative):')
        print(err)

