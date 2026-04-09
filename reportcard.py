student = { 'name': 'subh', 'marks': [90, 80, 70, 60, 50] }
def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average
if calculate_average(student['marks']) >= 50:
    print('pass')
else:
    print('fail')



student = input("enter the name of the student: ")

subjects = ['maths', 'physics', 'chemistry', 'english', 'computer science']
marks = []
for i in subjects:
    marks .append(int(input(f'enter the marks for {i}: ')))
average = sum(marks) / len(marks)
if average <= 40:
    print('fail')
elif average >= 40:
    print('pass')