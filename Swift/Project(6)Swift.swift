// CREATED AT 1/4/2019
// PROJECT NUMBER = 6
// LANGAUGE USED "SWIFT"
// This is a function to multiply a given set of numbers

// Variables
var product = 1
var multiplicants = [7,2,4]
var loop_stopper = 0
var index = 0

// Function Start
func Problem_Solving() -> Int
{
    while loop_stopper != multiplicants.count 
    {
        product = product * multiplicants[index]
        loop_stopper += 1
        index += 1
    }
    print(product)
    return product
}
Problem_Solving()