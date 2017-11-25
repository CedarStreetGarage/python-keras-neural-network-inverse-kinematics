from keras.models       import Sequential
from keras.layers       import Dense
from keras.regularizers import l2


L2_REGULARIZATION = 0.03
INITIALIZATION    = 'random_normal'
FIRST_ACTIVATIONS = 'relu'
LAST_ACTIVATION   = 'sigmoid'


class Model(object):

    def make(self):
        return self._make(3, [10, 10, 10], 3)


    def _make(self, first, hidden, last):
        model = Sequential()

        # First layer
        layer = Dense(input_dim          = first,
                      units              = hidden[0],
                      kernel_initializer = INITIALIZATION,
                      kernel_regularizer = l2(L2_REGULARIZATION),
                      use_bias           = True,
                      bias_initializer   = INITIALIZATION,
                      bias_regularizer   = l2(L2_REGULARIZATION),
                      activation         = FIRST_ACTIVATIONS)
        model.add(layer)

        # Hidden layers
        for i in range(len(hidden)-1):
            layer = Dense(units              = hidden[i+1],
                          kernel_initializer = INITIALIZATION,
                          kernel_regularizer = l2(L2_REGULARIZATION),
                          use_bias           = True,
                          bias_initializer   = INITIALIZATION,
                          bias_regularizer   = l2(L2_REGULARIZATION),
                          activation         = FIRST_ACTIVATIONS)
            model.add(layer)

        # Last layer
        layer = Dense(units              = last,
                      kernel_initializer = INITIALIZATION,
                      use_bias           = True,
                      bias_initializer   = INITIALIZATION,
                      activation         = LAST_ACTIVATION)
        model.add(layer)

        return model

