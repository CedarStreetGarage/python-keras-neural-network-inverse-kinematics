from keras.optimizers import Adam
from keras.callbacks  import ModelCheckpoint
from flow             import Flow
from model            import Model
from chain            import Chain
from generator        import Generator


class Train(object):

    def train(self):
        Flow().defaults()

        m = Model().make_fcn()
        m.summary()

        c = Chain().make()
        c.transform_summary()
        c.determinant_summary()

        print('_________________________________________________________________\n\n')

        o = Adam(lr=1.0e-3)
        m.compile(optimizer=o, loss='mse')

        mc = ModelCheckpoint(filepath       = 'model_weights.h5', 
                             verbose        = True, 
                             save_best_only = True)

        m.fit_generator(generator        = Generator().make(20), 
                        validation_data  = Generator().make(10),
                        steps_per_epoch  = 100, 
                        epochs           = 10,
                        validation_steps = 3,
                        callbacks        = [mc])

