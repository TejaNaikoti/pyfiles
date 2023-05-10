try:
    age = int(input("Age: "))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print("Age cannot be o ")
except ValueError:
    print("invalid value")
# else keyword defines a block of code to be excuted when no error were raised 
else:
    print("No Error")
# finally block, will be executed regardless if the try block raises an erroe or not

finally:
    print("completed")
    
