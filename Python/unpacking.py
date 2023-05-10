fruits = ("apple", "banana","cherry")
green , yellow, red = fruits
print(green,yellow,red)

cars = ("ford", "ferrari", "audi", "bmw", "ktm","royal enfield")
# ( '*' ) assings the rest of values to one variable
sports_car, f1_car, suoer, *sports_bike = cars
print(sports_car,sports_bike)
# if astrik (*) is added to another variable name other than the last,it will assign values to the variable untill the number of values left matches the number ofvariables left
fruit = ("mango", "pineapple", "orange", "grapes", "dragon fruit", "kiwi")
yellow, red, *healthy, green  = fruit
print(yellow , red, healthy, green)   