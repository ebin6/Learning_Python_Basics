
'''def Addition(a,b):
    return a+b

print(Addition(45,2))'''

'''v=lambda a,b:a+b
print(v(45,2))

is_even=lambda num:f"{num} is even" if num%2==0 else f"{num} is Odd"
n=int(input("Enter the number : "))
print(is_even(n))'''






numbers=[12,3,7,6,9,10]

print(list(map(lambda x:True if x%2==0 else False ,numbers)))
print(list(filter(lambda x:True if x%2==0 else False ,numbers)))

from functools import reduce

s=reduce(lambda a,b:a*b,range(1,6))
print(s)