// CREATED AT 1/5/2019
// PROJECT NUMBER = 7
// LANGAUGE USED "SWIFT"
// This function determines the biggest number in a set of numbers

var array = [2,6,1,4,9]
var x = 0
var y = 0
var z = 0
var max = array[y]
var checker = 0

func Problem_Solving()
{
    while x != array.count {
        if x == array.count {
            z = array.count - 1
        }
        checker = array[z]
        if checker > max {
            max = checker
        }
        z += 1
        x += 1
        y += 1
    }
    print("Done! Your biggest number is \(max)")
}
Problem_Solving()