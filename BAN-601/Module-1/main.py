e = """
Exercise 1
Write a function sum_product(a,b) that returns both the sum and the product
of two numbers, the result should be returned as a tuple (sum, product).
"""

def sum_product(a,b):
    print(e)
    a = (a + b)
    p = (a * b)
    return a, p

print(sum_product(5,30))

e = """
Exercise 2
Using sorted() function, write a function second_largest(num) that returns the
second largest number in a list of numbers.
For simplicity, you can assume the list has at least two distinct numbers.
"""

def second_largest():
    print(e)
    a = [399, 43, 654, 6, 76, 86] 

    a.sort() # modify the list in-place

    for i in sorted(a): # for testing purposes
        print(i)

    return a[-2] # return the second to last element in the list

print("Second Largest: => ",  second_largest())


e = """
Exercise 3
"""
