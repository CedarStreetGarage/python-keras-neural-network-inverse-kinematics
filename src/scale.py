class Scale(object):

    def __init__(self, src, dst):
        self.src_min = src[0]
        self.dst_min = dst[0]
        self.scale   = (dst[1] - dst[0]) / (src[1] - src[0])

    def forward_scale(self, x):
        return (x - self.src_min) * self.scale + self.dst_min

    def reverse_scale(self, y):
        return (y - self.dst_min) / self.scale + self.src_min

