# Variables
vector1 = [1, 2, 3, 4, 5, 7]
vector2 = [6, 7, 8, 9, 10, 12]

# Loop
def calc():
    if len(vector1) == len(vector2):
        index = 0
        summation = 0
        for val in vector1:
            summation += vector1[index] * vector2[index]
            index += 1
        print("Summation = " + str(summation))
    else:
        print("Error: Your vectors don't have same number of inputs")
# Output
calc()