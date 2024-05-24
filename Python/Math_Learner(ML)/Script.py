class NN:

    def think(self, I1, w1, I2, w2):
        print((I1 * w1) + (I2 * w2))

    def train(self, I1, w1, I2, w2, co, num):
        for iteration in range(num):
            print(iteration + 1)
            output = I1 * w1 + I2 * w2
            print("output is " + str(output))
            error = co - output
            # print("error is " + str(error))
            adjustment = 0.01 * (I1 * error + I2 * error)
            #print("adjustment is " + str(adjustment))
            w1 += adjustment
            w2 += adjustment
            #print("weights after adjusting")
            print("w1 = " + str(w1) + " w2 = " + str(w2))

NeNe = NN()
NeNe.think(2, 3, 1, 2)

# weight 1 = 2.0
# weight 2 = 2.0