from keras.models import Sequential
from keras.layers import Dense


class Model(object):

    def make_fcn(self):
        return self._make_fcn(3, [500, 500], 3)

    def _make_fcn(self, first, hidden, last):
        model = Sequential()

        # First layer
        layer = Dense(input_dim          = first,
                      units              = hidden[0],
                      kernel_initializer = 'random_normal',
                      use_bias           = True,
                      bias_initializer   = 'random_normal',
                      activation         = 'tanh')
        model.add(layer)

        # Hidden layers
        for i in range(len(hidden)-1):
            layer = Dense(units              = hidden[i+1],
                          kernel_initializer = 'random_normal',
                          use_bias           = True,
                          bias_initializer   = 'random_normal',
                          activation         = 'tanh')
            model.add(layer)

        # Last layer
        layer = Dense(units              = last,
                      kernel_initializer = 'random_normal',
                      use_bias           = True,
                      bias_initializer   = 'random_normal',
                      activation         = 'tanh')
        model.add(layer)

        return model

