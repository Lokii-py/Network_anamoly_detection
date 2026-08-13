import math

from source_code.utils.utils import clip_probablity

def loss(p, y):
    p = clip_probablity(p)
    penalty = - ((y * math.log(p)) + ((1-y)*(math.log(1-p))))
    return penalty