// CREATED AT 12/18/2018
// PROJECT NUMBER = 2
// LANGAUGE USED "SWIFT"
// Prints the smallest number in a set of numbers

var array = [2,6,1,4]
var x = 0 // loop_stopper
var y = 0 // 
var z = 0 // index
var min = array[y]
var checker = 0

func Problem_Solving()
{
    while x != array.count {
        if x == array.count {
            z = array.count - 1
        }
        checker = array[z]
        if checker > min {
            min = checker
        }
        z += 1
        x += 1
        y += 1
    }
    print("Done! Your min number is \(min)")
}
Problem_Solving()