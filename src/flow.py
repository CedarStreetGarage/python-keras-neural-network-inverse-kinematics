import os 


class Flow(object):

    def defaults(self):
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
