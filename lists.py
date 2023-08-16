num_students = int(input("How many students are there?: "))
student_list = []
student_info = []

for i in range(num_students):
    num_marks = int(input("How many marks does this student have?: "))
    marks = []
    for i in range(num_marks):
        mark = float(input("Enter the mark: "))
        marks.append(mark)

    average = sum(marks) / num_marks
    max_mark = max(marks)
    min_mark = min(marks)

    student_info = [marks, average, max_mark, min_mark]
    student_list.append(student_info)

counter = 1
for i in student_list:
    print("-----------------------------------------------------------")
    print(f"Student {counter} Info:")
    counter += 1
    print(f"Student Marks: {i[0]}")
    print(f"Student Average Marks: {i[1]}")
    print(f"Student MAX Marks: {i[2]}")
    print(f"Student MIN Marks: {i[3]}")
