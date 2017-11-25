from keras.models import Sequential
from keras.layers import Dense
from keras.regularizers import l2


class Model(object):

    def make(self):
        return self._generate(3, [20, 50, 50, 20], 3)


    def _generate(self, first, hidden, last):
        model = Sequential()

        # First layer
        layer = Dense(input_dim          = first,
                      units              = hidden[0],
                      kernel_initializer = 'random_normal',
                      kernel_regularizer = l2(0.03),
                      use_bias           = True,
                      bias_initializer   = 'random_normal',
                      bias_regularizer   = l2(0.03),
                      activation         = 'relu')
        model.add(layer)

        # Hidden layers
        for i in range(len(hidden)-1):
            layer = Dense(units              = hidden[i+1],
                          kernel_initializer = 'random_normal',
                          kernel_regularizer = l2(0.03),
                          use_bias           = True,
                          bias_initializer   = 'random_normal',
                          bias_regularizer   = l2(0.03),
                          activation         = 'relu')
            model.add(layer)

        # Last layer
        layer = Dense(units              = last,
                      kernel_initializer = 'random_normal',
                      use_bias           = True,
                      bias_initializer   = 'random_normal',
                      activation         = 'sigmoid')
        model.add(layer)

        return model

