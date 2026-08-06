import math
import random

class Model:
    def __init__(self, num_weights = 3):
        """Initialize the model weight"""
        self.weights = []
        for _ in range(num_weights):
            self.weights.append(random.random())
        self.bias = random.random()

    def sigmoid(self, z: float):
        return 1 / (1 + math.exp(-z))
    
    def forward(self, inputs):
        """Get the input and multiply with model weight"""
        assert len(inputs) == len(self.weights), "The number of input should be equal to num of weights"
        z = 0
        for feature, weight in zip(inputs, self.weights):
            z += feature * weight
        z += self.bias
        return self.sigmoid(z)