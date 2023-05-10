try:
    print(X)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
