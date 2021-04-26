#recursions
#factorial
def factorial(x):
    if x==1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))
print("------------------------\n") 

#fibonaaci
def fib(x):
    if(x == 0 or x == 1 ):
        return 1
    else:
        return fib(x-1) + fib(x-2)
    
print(fib(4))
print("------------------------\n")

#odd even using recusrion
def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)

print(is_even(5))
print(is_odd(5))
print("------------------------\n")

#sets
number_sets = {3, 7, 8}
another_set = set([3, 7, 8])

print(8 in number_sets)
print(3 in another_set)
print(9 in number_sets)
print("------------------------\n")

#sets functions
#to add an item
number_sets.add(32)
number_sets.add(43)
print(number_sets)

#to remove an item
number_sets.remove(32)
print(number_sets)

number_sets.pop()
print(number_sets)

#length
print(len(number_sets))

print("------------------------\n")

#set operations on two sets

#gets union: items in either of sets
print(number_sets | another_set)

#gets intersection: items only in both
print(number_sets & another_set)

#gets difference: items in fisrt but not second
print(number_sets - another_set)
print(another_set - number_sets)

#gets symmetric difference: items in either but not both
print(number_sets ^ another_set)

print("------------------------\n")

#itertool standard library
from itertools import accumulate, takewhile, product, count as ct

#count function
for i in ct(3):
    print(i)
    if i >= 11:
        break
print("------------------------\n")

#accumulate
nums = list(accumulate(range(5)))
print(nums)

#takewhile
print(list(takewhile(lambda x: x <= 6, nums)))

#product
a = {1, 2}

print(list(product(range(3), a)))
print("------------------------\n")