user_name = input("What is your name: ")
quiz_score = float(input("What is your quiz score: "))
assignment_score = float(input("What is your assignment score: "))
project_score = float(input("What is your project score: "))
lab_score = float(input("What is your lab score: "))

for midterm_exam in range(0, 101, 20):
    final_grade = (55 * midterm_exam + 15 * quiz_score + 10 * assignment_score + 10 * project_score + 10 * lab_score) / 100
    print(f"{user_name}, if your average midterm exam is {midterm_exam}, your course percentage for CS1400 will be: {final_grade}.")