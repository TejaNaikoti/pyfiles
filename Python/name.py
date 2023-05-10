from tarfile import LENGTH_NAME
from unittest.util import strclass


name = str(input('name: '))
if len(name) < 3:
    print("Name must be at least of 3 characters")
elif len(name) > 50:
    print("Name should be less than 50 characters")
else:
    print("name looks Good")
