from keras.models import Sequential
from keras.layers import Dense


class Model(object):

    def make(self, first, hidden, last):
        model = Sequential()
        model.add(Dense(hidden[0], 
                        input_dim          = first, 
                        activation         = 'relu', 
                        kernel_initializer = 'random_normal'
        ))
        for i in range(len(hidden)-1):
            model.add(Dense(hidden[i+1], 
                            activation         = 'relu', 
                            kernel_initializer = 'random_normal'
            ))
        model.add(Dense(last, 
                        activation         = 'sigmoid', 
                        kernel_initializer = 'random_normal'
        ))
        return model


