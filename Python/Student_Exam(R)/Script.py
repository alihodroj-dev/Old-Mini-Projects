# imports

# variables
passed_file_read = open("Passed.txt", "r")
grades_array = []  # store
failure_grades = []

# starting statements
for grade1 in passed_file_read.readlines():
    grades_array.append(grade1)

# classes
class NeuralNetwork:
    # Training
    def train(self, insertvalue):
        if insertvalue != "":
            passed_file_write = open("Passed.txt", "w")
            grades_array.append("\n" + insertvalue)
            for grade2 in grades_array:
                passed_file_write.write(grade2)
    # Checking
    def check(self, checkedValue):
        if checkedValue != "":
            numberOfGrades = 0
            totalNumberOfGrades = 0
            for grade3 in grades_array:
                numberOfGrades += 1
                totalNumberOfGrades += int(grade3)
                average = totalNumberOfGrades / numberOfGrades
            if int(checkedValue) >= int(average):
                print("Average is " + str(int(average)))
                print("Student Passed")
            else:
                print("Average is " + str(int(average)))
                print("Student Failed")
        else:
            print("Please Enter A Grade")

# objects
Network = NeuralNetwork
Network.train("", "")
Network.check('', '14')