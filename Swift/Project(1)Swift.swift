// CREATED AT 12/17/2018
// PROJECT NUMBER = 1
// LANGAUGE USED "SWIFT"
//This function determines in which place is the number

func Problem_Solving(num: Int) {
    if num < 10 {
        print("Your number is in the ones place!")
        
    }else if num >= 10 && num < 100{
        print("Your number is in the tens place!")
    }else if num >= 100 && num < 1000 {
        print("Your number is in the hundreds place!")
    }else if num >= 1000 && num < 10000 {
        print("Your number is in the thousands place!")
    }else if num >= 10000 && num < 100000{
        print("Your number is in the ten thousands place!")
    }else if num >= 100000 && num < 1000000 {
        print("Your number is in the hundreds thousands place!")
    }else if num >= 1000000 && num < 100000000 {
        print("Your number is in the millions place!")
    }
}

Problem_Solving(num: 4)