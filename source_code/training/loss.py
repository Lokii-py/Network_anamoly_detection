import math

def loss(p, y):
    penalty = - ((y * math.log(p))+ ((1-y)*(math.log(1-p))))
    return penalty