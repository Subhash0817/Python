
from webbrowser import get


movies = ['Bahubali', 'kgf', 'kalki', 'billa', 'darling' ]
movies_2 = ['mirchi', 'rrr']
movies.extend(movies_2)
movies.remove('billa')
print(len(movies))

print (movies[0])
print (movies[3])
print (movies[-1])


numbers = [1, 2, 3, 4, 5]
for i in numbers:
    print(i*2)


tuple_1 = ('subh','cse',2026, '7.75')
tuple_2 = tuple_1

tuple_1[0] = 'subhash'

"""tuples are immutable, we cannot change the value of a tuple once it is created."""

print(tuple_1)
print(tuple_2)


highest_marks = (95, 90, 85, 80, 75)
print(max(highest_marks))

 





