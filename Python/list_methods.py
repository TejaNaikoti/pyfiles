list = [1 , 3, 4, 1, 3, 10, 3, 3, 6, 9]
numbers = [99, 8, 7, 4, 1, 6, 5, 10]

# 1 sort(): arranges a list in a ascending order
list.sort()
print(list)

# 2 index(): returns a index value of that number
print(list.index(4))

# 3 count():counts a number in a list and gives its counted value
print(list.count(3))

# 4 reverse(): reverse a list  
numbers.reverse()
print(numbers)

# 5 append() adds a value at the end of the list
list.append(10)
print(list)

#6 insert() method inserts a number in a list. (insert(index,object))
list.insert(1,2)
print(list)

# 7 remove() menthod removes a number in a list
list.remove(2)
print(list)
 
 # 8 pop(): removes a last element in a list
numbers.pop()
print(numbers)

# 9 copy(): copies a list
list2= list.copy()
print(list2)  

# 10 clear(): removes all the elements in a list
list.clear()
print(list)

# 11.extend(): add the elements of a list(any iterables), to the end of the list
items =("car", "bike", "train")
numbers.extend(items)
print(numbers)
