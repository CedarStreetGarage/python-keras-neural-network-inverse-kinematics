from keras.models       import Sequential
from keras.layers       import Dense, Dropout


DROPOUT_AMOUNT    = 0.3
INITIALIZATION    = 'random_normal'
FIRST_ACTIVATIONS = 'relu'
LAST_ACTIVATION   = 'sigmoid'


class Model(object):

    def make(self):
        return self._make(3, [50, 50], 3)

    def _make(self, first, hidden, last):
        model = Sequential()

        # First layer
        layer = Dense(input_dim          = first,
                      units              = hidden[0],
                      kernel_initializer = INITIALIZATION,
                      use_bias           = True,
                      bias_initializer   = INITIALIZATION,
                      activation         = FIRST_ACTIVATIONS)
        model.add(layer)
        model.add(Dropout(DROPOUT_AMOUNT))

        # Hidden layers
        for i in range(len(hidden)-1):
            layer = Dense(units              = hidden[i+1],
                          kernel_initializer = INITIALIZATION,
                          use_bias           = True,
                          bias_initializer   = INITIALIZATION,
                          activation         = FIRST_ACTIVATIONS)
            model.add(layer)
            model.add(Dropout(DROPOUT_AMOUNT))

        # Last layer
        layer = Dense(units              = last,
                      kernel_initializer = INITIALIZATION,
                      use_bias           = True,
                      bias_initializer   = INITIALIZATION,
                      activation         = LAST_ACTIVATION)
        model.add(layer)

        return model

