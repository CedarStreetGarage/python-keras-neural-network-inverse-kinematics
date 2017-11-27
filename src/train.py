from keras.optimizers import Adam
from keras.callbacks  import ModelCheckpoint
from flow             import Flow
from model            import Model
from chain            import Chain
from generator        import Generator


class Train(object):

    def train(self):
        Flow().defaults()

        m = Model().make()
        m.summary()

        Chain().make().summary()

        o = Adam(lr=1.0e-3)
        m.compile(optimizer=o, loss='mse')

        mc = ModelCheckpoint(filepath       = 'model_weights.h5', 
                             verbose        = True, 
                             save_best_only = True)

        m.fit_generator(generator        = Generator().make(50), 
                        validation_data  = Generator().make(20),
                        steps_per_epoch  = 20, 
                        epochs           = 20,
                        validation_steps = 3,
                        callbacks        = [mc])

