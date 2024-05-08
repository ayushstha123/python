#In Python, lambda is a keyword used to create anonymous functions, also known as lambda functions. These functions are small, one-line functions that can have any number of arguments but only one expression.

squared=lambda num:num*num
print(squared(2))

addTwo =lambda num:num+2
print(f"adding two : {addTwo(2)}")

sum=lambda a,b:a+b
print("The sum :" + str(sum(1,2)))

######HOW LAMBDA WORKS
def funcBuilder(x):
    return lambda num:num+x

addTwo=funcBuilder(2)
addTen=funcBuilder(10)

print(addTwo(3))
print(addTen(10))

#####what is a higher order function
#A higher order function is a function that takes one or more functions as an argument or a function that returns a function as a result
# The map() function in Python is a higher-order built-in function that applies a given function to each item of an iterable (such as a list, tuple, or string) and returns a map object (an iterator) that yields the results.
#syntax: map(function, iterable, ...)


numbers=[1,2,3,4,5,6,7]
squared_nums=map(lambda num:num*num,numbers)
print(list(squared_nums))

########### filter ########
# The filter() function in Python is another higher-order built-in function that constructs an iterator from elements of an iterable for which a function returns True. It's similar to map(), but instead of applying a function to each item, it filters the items based on whether the function evaluates to True or False for each item.
odd_num=filter(lambda num:num%2 != 0 ,numbers)
print(list(odd_num))


######### reduce  ########
from functools import reduce
numbers=[1,2,3,4,5,6,7]
total=reduce(lambda acc,curr:acc + curr,numbers)
print(total)