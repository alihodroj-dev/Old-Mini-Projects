// CREATED AT 12/21/2018
// PROJECT NUMBER = 4
// LANGAUGE USED "SWIFT"
// This function determines the time needed to reach your destination

// Variables
var currentX = 0
var currentY = 0
var way1_pointX = 5
var way1_pointY = 5
var way2_pointX = 4
var way2_pointY = 9
var way1_steps = 0
var way2_steps = 0
var destinationX = 0
var destinationY = 10
var which_way = 0
var way_p = ""
var time = 0
var timeOverHour = 0
var hours = 0

func Problem_Solving(traffic: String, way1_blocked: Bool, way2_blocked: Bool)
{
    // Caculating distance
    way1_steps = way1_pointX - currentX
    way1_steps += way1_pointY - currentY
    way1_steps += destinationX + way1_pointX
    way1_steps += destinationY - way1_pointY
    way2_steps = way2_pointX - currentX
    way2_steps += way2_pointY - currentY
    way2_steps += destinationX + way2_pointX
    way2_steps += destinationY - way2_pointY
    // Checking for roadblocks
    if way1_blocked == true && way2_blocked != true {
        for km in 1...way2_steps {
            time += 1
        }
        if traffic == "light" {
            time = time * 1 + time / 2
        }else if traffic == "medium" {
            time = time * 2 + time / 2
        }else if traffic == "heavy" {
            time = time * 4
        }
        print("Distance from your location to your destination is \(way2_steps) km through way2")
        if time > 60 {
            hours = time / 60
            timeOverHour = time - hours * 60
            print("Time needed to reach your destination is \(hours) hour and \(timeOverHour) minutes")
        }else{
            print("Time needed to reach your destination is \(time) minutes")
        }
        }else if way2_blocked == true && way1_blocked != true {
            for km in 1...way1_steps {
                time += 1
            }
            if traffic == "light" {
                time = time * 1 + time / 2
            }else if traffic == "medium" {
                time = time * 2 + time / 2
            }else if traffic == "heavy" {
                time = time * 4
            }
            print("Distance from your location to your destination is \(way1_steps) km through way1")
            if time > 60 {
                hours = time / 60
                timeOverHour = time - hours * 60
                print("Time needed to reach your destination is \(hours) hour and \(timeOverHour) minutes")
            }else{
                print("Time needed to reach your destination is \(time) minutes")
            }
        }else if way1_blocked == true && way2_blocked == true {
            print("All ways are blocked. You better stay at home!")
        }
    // Deciding which way to take
    if way1_steps > way2_steps {
        which_way = way1_steps
    }else {
        which_way = way2_steps
    }
    // Calculating time
    for km in 1...which_way {
        time += 1
    }
    // Checking for traffic
    if traffic == "light" {
        time = time * 1 + time / 2
    }else if traffic == "medium" {
        time = time * 2 + time / 2
    }else if traffic == "heavy" {
        time = time * 4
    }
    if which_way == way1_steps {
        way_p = "Way 1"
    }else {
        way_p = "Way 2"
    }
    // Giving output
    if way1_blocked == false && way2_blocked == false {
        print("Distance from your location to your destination is \(which_way) KM through \(way_p)")
        if time > 60 {
            hours = time / 60
            timeOverHour = time - hours * 60
            if hours == 1 && timeOverHour == 0 {
                print("Time needed to reach your destination is \(hours) hour")
            }else if hours == 1 && timeOverHour != 0 {
                if timeOverHour == 1 {
                    print("Time needed to reach your destination is \(hours) hour and \(timeOverHour) minute")
                }else {
                    print("Time needed to reach your destination is \(hours) hour and \(timeOverHour) minutes")
                }
            }else if hours > 1 && timeOverHour == 0 {
                print("Time needed to reach your destination is \(hours) hours")
            }else if hours > 1 && timeOverHour != 0 {
                if timeOverHour == 1 {
                    print("Time needed to reach your destination is \(hours) hours and \(timeOverHour) minute")
                }else {
                    print("Time needed to reach your destination is \(hours) hours and \(timeOverHour) minutes")
                }
            }
        }else {
            if time == 1 {
                print("Time needed to reach your destination is \(time) minute")
            }else {
                print("Time needed to reach your destination is \(time) minutes")
            }
        }
    }
}

Problem_Solving(traffic: "light", way1_blocked: false, way2_blocked: false)