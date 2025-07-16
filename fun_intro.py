"""
Syntax

def Function_name():
    statements




"""

def Fact(num):
    f = count = 1
    while count <= num:
        f = f * count
        count += 1
    print(f)

Fact(5)
Fact(4)
Fact(7)



"""
def is_even(num):
    if num%2==0:
        print(num,"is even")
    else:
        print(num,"is Odd")


def is_positive(num):
    if num>=0:
        return True
    else:
       return False

num=int(input("Enter the number : "))
if is_positive(num):
    is_even(num)
else:
    print("PLease enter a positive number")
"""
def Total(numbers):
   d=0
   for i in numbers:
       d=d+i
   return d

my_list=[45,12,8,3]

s=Total(my_list)

print(s/len(my_list))