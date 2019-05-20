# This program will help the user to weighted different types of grade and
# generate a final weighted course grade. Users input the information of each exam and
# homework. The program will use this information to create a final weighted
# grade. Then we can use the final weighted grade to determine the minimum GPA
# that the user will get.

# This function is for the weighted exam scores. Input the name of the exam
# and the function will return the weighted score for this exam.
def exam(name):
    print(name, end = '')
    print(":")
    weight_amount = input("Weight (0-100)? ")
    score = input("Score earned? ")
    shifted_or_not = input("Were scores shifted (1=yes, 2=no)? ")
    # The program will stop running if the input is not either 1 or 2.
    if int(shifted_or_not) != 1 and int(shifted_or_not) != 2:
        print("Incorrect value, the program ends")
        exit()
    elif int(shifted_or_not) == 1:
        shift_amount = input("Shift amount? ")
        score = float(score) + float(shift_amount)
        if score > 100:
            score = 100
    print("Total points = ", score, "/ 100")
    weighted_score = float(score) * float(weight_amount) / 100
    print("Weighted score = ", weighted_score, "/", weight_amount)
    print()
    return weighted_score

# This function is to determine the weighted score of the homework, and it will
# return the weighted score of the sum of the homeworks and section grades.
def homework():
    print("Homework:")
    weight_hw = input("Weight (0-100)? ")
    number_of_hw = input("Number of assignments? ")
    total_hw = 0
    max_hw = 30
    for i in range(1, int(number_of_hw)+1):
        score, max = input("Assignment " + str(i) +  " score and max? ").split()
        total_hw = total_hw + float(score)
        max_hw = max_hw + float(max)
    section_attend = input("How many sections did you attend? ")
    while  int(section_attend) > 6:
        print("Exceed the maximum amount, the program end")
        exit()
    print("Section points = ", 5 * int(section_attend),"/ 30")
    total_hw = 5 * int(section_attend) + total_hw
    print("Total points = ", float(total_hw), "/ ", float(max_hw))
    # Floor the weighted score down to one decimal number.
    weighted_hw_score = float(total_hw) * float(weight_hw) * 10 // float(max_hw) / 10
    print("Weighted score = ", weighted_hw_score, "/ ", float(weight_hw))
    print()
    return weighted_hw_score


print("This program reads exam/homework scores")
print("and reports your overall course grade.")
print()
midterm_score = exam("Midterm")
final_score = exam("Final")
hw_score = homework()
# Calculate the weighted total score
total_score = midterm_score + final_score + hw_score
print("Overall percentage = ", total_score)
# Caculate GPA based on the weighted overall grade.
if total_score >= 85:
    gpa = 3.0
elif total_score >= 75:
    gpa = 2.0
elif total_score >= 60:
    gpa = 0.7
else:
    gpa = 0.0
print("Your grade will be at least: ", gpa)
if total_score >= 85:
    print("Good job bro!!")
elif total_score >= 75:
    print("At least you will get the credits!")
elif total_score >= 60:
    print("Keep studying hard.")
else:
    print("Drop the class for your own good.")
