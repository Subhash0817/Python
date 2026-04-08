tuple_cities = ('hyderabad', 'chennai', 'bangalore', 'mumbai', 'delhi')
tuple_cities_2 = tuple_cities
tuple_cities_2[0] = 'shimla'

for index, city in enumerate(tuple_cities, start=1):
    print(f'{index}: {city}')
# tuples are immutable, we cannot change the value of a tuple once it is created.