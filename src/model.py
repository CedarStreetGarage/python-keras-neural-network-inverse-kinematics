from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.regularizers import l2


class Model(object):

    def make(self, first, hidden, last):
        model = Sequential()

        # First layer
        layer = Dense(input_dim          = first,
                      units              = hidden[0],
                      kernel_initializer = 'random_normal',
                      bias_initializer   = 'random_normal',
                      W_regularizer      = l2(0.02),
                      activation         = 'relu')
        model.add(layer)
        model.add(Dropout(0.2))

        # Hidden layers
        for i in range(len(hidden)-1):
            layer = Dense(units              = hidden[i+1],
                          kernel_initializer = 'random_normal',
                          bias_initializer   = 'random_normal',
                          W_regularizer      = l2(0.02),
                          activation         = 'relu')
            model.add(layer)
            model.add(Dropout(0.2))

        # Last layer
        layer = Dense(units              = last,
                      kernel_initializer = 'random_normal',
                      bias_initializer   = 'random_normal',
                      W_regularizer      = l2(0.02),
                      activation         = 'sigmoid')
        model.add(layer)

        return model


