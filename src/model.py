from keras.models import Sequential
from keras.layers import Dense


class Model(object):

    def make(self, first, hidden, last):
        model = Sequential()

        # First layer
        layer = Dense(input_dim          = first,
                      units              = hidden[0],
                      kernel_initializer = 'random_normal',
                      bias_initializer   = 'random_normal',
                      activation         = 'relu')
        model.add(layer)

        # Hidden layers
        for i in range(len(hidden)-1):
            layer = Dense(units              = hidden[i+1],
                          kernel_initializer = 'random_normal',
                          bias_initializer   = 'random_normal',
                          activation         = 'relu')
            model.add(layer)

        # Last layer
        layer = Dense(units              = last,
                      kernel_initializer = 'random_normal',
                      bias_initializer   = 'random_normal',
                      activation         = 'sigmoid')
        model.add(layer)

        return model


