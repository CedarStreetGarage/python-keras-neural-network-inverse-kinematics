from model import Model
from generator import Generator
from keras.optimizers import Adam
from keras.callbacks  import ModelCheckpoint


model = Model().make(3, [20, 20], 3)
model.summary()

opt = Adam(lr=1.0e-3)
model.compile(optimizer=opt, loss='mse')

checkpoint = ModelCheckpoint(filepath       = 'model_weights.h5', 
                             verbose        = True, 
                             save_best_only = True)

model.fit_generator(generator        = Generator().make(20), 
                    validation_data  = Generator().make(10),
                    steps_per_epoch  = 20, 
                    epochs           = 10, 
                    validation_steps = 2,
                    callbacks        = [checkpoint])

