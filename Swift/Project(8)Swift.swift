// CREATED AT 1/7/2019
// PROJECT NUMBER = 8
// LANGAUGE USED "SWIFT"
// This is a SORTING ALGORITHMN

// Variables
var arr1 = [2,6,3,7,1]
    var arr2 = [0]
        var loop1_stopper = 0
            var loop2_stopper = 0
                var loop3_stopper = 0
                    var smallest = arr1[0]
                var checker_index = 0
            var checker = arr1[checker_index]
        var arr_count = arr1.count - 1
    var removed_index = 0
var loop3_index = 0

// Function Start
func Problem_Solving() {
    // First While loop Start
    while loop1_stopper != arr_count {
        // Second While loop Start
        while loop2_stopper != arr1.count {
            checker = arr1[checker_index]
            if checker < smallest {
                smallest = checker
                removed_index = checker_index
            }   
            checker_index += 1
            loop2_stopper += 1
            // Second While loop End
        }
        arr2.append(smallest)
            arr1.remove(at:removed_index)
                loop2_stopper = 0
                        loop1_stopper += 1
                    smallest = arr1[0]
                removed_index = 0
            checker_index = 0
        checker = arr1[checker_index]
        // First While loop End
    }
    arr2.append(arr1[0])
        arr2.remove(at:0)
    // Third While loop Start
    while loop3_stopper != arr2.count {
        print(arr2[loop3_index])
            loop3_index += 1
            loop3_stopper += 1
        // Third While loop End
    }
}
// Function End
Problem_Solving()