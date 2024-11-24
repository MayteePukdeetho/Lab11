import matplotlib.pyplot as plt
import os
from pathlib import Path
def load():
    students = []
    with open('data/students.txt') as file:
        for line in file:
            line = line.strip()
            id = line[:3]
            name = line[3:]
            id = int(id)
            students.append([id, name])


    assignments = []

    with open('data/assignments.txt') as file:
        lines = file.readlines()
        for assignment in range(0, len(lines), 3):
            assignment_name = lines[assignment].strip()
            assignment_id = int(lines[assignment+1].strip())
            assignment_points = int(lines[assignment+2].strip())
            assignments.append([assignment_name, assignment_id, assignment_points])

    submissions = []
    for file_name in os.listdir('data/submissions'):
        file_path = os.path.join('data/submissions', file_name)
        with open(file_path, 'r') as file:
            for line in file:
                id, assignment, grade = line.strip().split('|')
                id = int(id)
                assignment = int(assignment)
                grade = int(grade)
                submissions.append([id, assignment, grade])


    return students, assignments , submissions



students, assignments, submissions = load()
total_grade = 0
for assignment in assignments:
   assignment_weight = assignment[2]
   assignment = assignment_weight * 100
   total_grade += assignment
#print(total_grade)
#print(submissions)
option = int(input("1. Student grade\n2. Assignment statistics\n3. Assignment graph\n\nEnter your selection: "))
if option == 1:


    chosen_name = input("What is the student's name: ")
    current_student_total_grade = 0
    for student_data_block in students:
        if student_data_block[1] == chosen_name:
            chosen_student_id = student_data_block[0]
            for submission in submissions:
                if chosen_student_id == submission[0]:
                    current_grade = submission[2]
                    for assignment in assignments:
                        if assignment[1] == submission[1]:
                            current_grade_weight = assignment[2]
                            weighted_assignment_grade = current_grade * current_grade_weight
                            current_student_total_grade += weighted_assignment_grade



            print(int(round((100*(current_student_total_grade/total_grade)))),end='')
            print("%")
    if current_student_total_grade == 0:
        print('Student not found')

elif option == 2:
    chosen_assignment_name = input("What is the assignment name: ")
    for assignment_data_block in assignments:
        if assignment_data_block[0] == chosen_assignment_name:
            lowest_submission_grade = 100
            highest_submission_grade = 0
            aveage_submission_grade = 0
            submissions_for_assignment = 0
            chosen_assignment_id = assignment_data_block[1]
            for submission in submissions:
                if chosen_assignment_id == submission[1]:
                    current_submission_grade = submission[2]
                    if current_submission_grade < lowest_submission_grade:
                        lowest_submission_grade = current_submission_grade
                    if current_submission_grade > highest_submission_grade:
                        highest_submission_grade = current_submission_grade
                    aveage_submission_grade += current_submission_grade
                    submissions_for_assignment += 1
            print(f'Min: {int(lowest_submission_grade)}%')
            print(f'Avg: {int(aveage_submission_grade / submissions_for_assignment)}%')
            print(f'Max: {int(highest_submission_grade)}%')

    if highest_submission_grade == aveage_submission_grade:
        print('Assignment not found.')

elif option == 3:
    scores = []
    chosen_assignment_name = input('What is the assignment name: ')
    for assignment_data_block in assignments:
        if assignment_data_block[0] == chosen_assignment_name:
            chosen_assignment_id = assignment_data_block[1]
            for submission in submissions:
                if chosen_assignment_id == submission[1]:
                    current_submission_grade = submission[2]
                    scores.append(current_submission_grade)
    plt.hist(scores, bins=[60,63,67,70,73,77,80,83,87,90,93,97,100])
    plt.show()