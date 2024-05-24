# Inputs
inputs = [[1, 0, 1], [1, 0, 1], [0, 1, 0], [2, 1, 2], [0, 2, 0], [2, 0, 2]]


class NeuralNetwork:

    def __init__(self, w1, w2):
        self.w1 = w1
        self.w2 = w2

    def think(self, i1, i2):
        return i1 * self.w1 + i2 * self.w2

    def train(self):
        for iteration in range(10):
            for inp in inputs:
                op = self.think(inp[0], inp[1])
                error = inp[2] - op
                adjustment = .25 * (error * inp[0] + error * inp[1])
                self.w1 += adjustment
                self.w2 += adjustment


NN = NeuralNetwork(.1, .9)
NN.train()
print(NN.think(5, 1))
