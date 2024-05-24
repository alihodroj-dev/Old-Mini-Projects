// CREATED AT 12/23/2018
// PROJECT NUMBER = 5
// LANGAUGE USED "SWIFT"
// This is a to do list

var ToDoList = ["Check your algorithm"]
var priorities = ["Check your email"]
var ToDoDate = ["12:00 28/12/18"]
var prioritiesDate = ["10:00 29/12/18"]
var index = 0
var loop1_stoppper = 0
var loop2_stopper = 0
var number = 1

func Problem_Solving(print_ToDoList: Bool, print_prio: Bool, want_to_append: Bool, value_to_append: String, where_to_append: Int, when_to_do: String, 
want_to_append_to_prio: Bool, what_to_append_to_prio: String, where_to_append_in_prio: Int, when_to_do_added_prio: String)
{
    if want_to_append == true {
        ToDoList.insert(value_to_append, at: where_to_append)
        ToDoDate.insert(when_to_do, at: where_to_append)
    }
    if want_to_append_to_prio == true {
        priorities.insert(what_to_append_to_prio, at: where_to_append_in_prio)
        prioritiesDate.insert(when_to_do_added_prio, at: where_to_append_in_prio)
    }
    if print_ToDoList == true {
        print("ToDoList:")
        while loop1_stoppper != ToDoList.count {
            print("\(number)) \(ToDoList[index]) at \(ToDoDate[index])")
            index += 1
            loop1_stoppper += 1
            number += 1
        }
        index = 0
        number = 1
    }
    if print_prio == true {
    print("Priorities:")
        while loop2_stopper != priorities.count {
            print("\(number)) \(priorities[index]) at \(prioritiesDate[index])")
            index += 1
            loop2_stopper += 1
            number += 1
        }
        index = 0
        number = 1
    }
}

Problem_Solving(print_ToDoList: true, print_prio: true, want_to_append: false, value_to_append: "Talk to your dad", where_to_append: 1, when_to_do: "08:00 31/12/18", 
want_to_append_to_prio: false, what_to_append_to_prio: "Talk to your daddy", where_to_append_in_prio: 1, when_to_do_added_prio: "11:00 1/1/19")