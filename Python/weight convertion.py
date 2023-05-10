weight = int(input('weight: '))
unit = input("(L)bs or (K)gs: ")
if unit.upper() =="L":
    converted = weight*0.45
    print(f"you r {converted} kgs")
else:
    converted = weight/0.45
    print(f'u r {converted} pounds')