from model import Model
from generator import Generator
from keras.optimizers import Adam
from keras.callbacks  import ModelCheckpoint


model = Model().make()
model.summary()

opt = Adam(lr=1.0e-3)
model.compile(optimizer=opt, loss='mse')

checkpoint = ModelCheckpoint(filepath       = 'model_weights.h5', 
                             verbose        = True, 
                             save_best_only = True)

model.fit_generator(generator        = Generator().make(50), 
                    validation_data  = Generator().make(20),
                    steps_per_epoch  = 20, 
                    epochs           = 30,
                    validation_steps = 3,
                    callbacks        = [checkpoint])

