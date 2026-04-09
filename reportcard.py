student = { 'name': 'subh', 'marks': [90, 80, 70, 60, 50] }
def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average
if calculate_average(student['marks']) >= 50:
    print('pass')
else:
    print('fail')