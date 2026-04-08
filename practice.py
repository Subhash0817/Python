from numpy import add, number


name = 'subh'
age = 21
city = 'hyderabad'
message = f'{name}\n {age}\n {city}'
print(message)




is_btech ='true'
print(f"am i a btech student? {is_btech}")





name = 'subh'
age = 21
message = f'my name is {name} and i am {age} years old'
print(message)




num = 10
num1 = 20
sum = num + num1

print(f'the sum of {num} and {num1} is {sum}')


print(type(name))
print(type(age))
print(type(is_btech))
print(type(sum))



num = -5
if num > 0:
    print(f'{num} is a positive number')
elif num < 0:
    print(f'{num} is a negative number')
else:
    print(f'{num} is zero')


CGPA = 7.75
if CGPA >= 9:
    print('Distinction')
elif CGPA >= 7:
    print('First class')
else:
    print('fail')





num = 17
num1 = 8
if num > num1:
    print(f'{num} is bigger than {num1}')
elif num < num1:
    print(f'{num1} is bigger than {num}')
else:
    print(f'{num} and {num1} are equal')


num = 17
if num % 2 ==0:
    print(f'{num} is a even number')
else:
    print(f'{num} is a odd number')



for i in range(1, 11):
    print(i)

for  i in range(1, 20):
    if i%2 ==0:
        print(f'{i} is an even number')

for i in range(1, 20):
    if i%2 != 0:
        print(f'{i} is an odd number')  

for i in range(1, 11):
    print(f'{5} x {i} = {5*i}')

    


def add(a,b):
    return a + b
result = add(10, 20)
print(f'the sum of 10 and 20 is {result}')


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
number = 17
if is_even(number):
    print(f'{number} is an even number')        
else:    print(f'{number} is an odd number')




def table(n):
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')
number = 5
table(number)   
