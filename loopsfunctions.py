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

