'''age=int(input("Enter your age : "))'''


"""
Syntax 

if condition:
    statements 
else:
    statements
    
"""

'''if age>=18:
    print("Eligible for voting")
    print("Please get your voters id ")
else:
    print("Not eligible for voting")'''

# number =int(input("Enter the number : "))
# if number %2==0:
#     print(number,"is even")
# else:
#     print(number,"is odd")


'''year=int(input("Enter the year : "))
if (year%4==0 and year%100!=0) or year%400==0:
    print(year,"is a leap year")
else:
    print(year,"is not leap year")'''

'''payment_status=False
mark=int(input("Enter your mark : "))
if payment_status:
    if mark>60:
        print("Eligible for writting exam")
    else:
        print("Please increase your model exam marks")
else:
    print("Please complete your payment")'''
while True:
    a=int(input("Enter the first number : "))
    b=int(input("Enter the second number : "))
    print("Please enter your choice :\n 1.Addition \n 2.Substarction\n3.Multiplication\n4.Division")
    choice=int(input("Enter your choice 1,2,3,4 : "))
    if choice==1:
        print(a+b)
    elif choice==2:
        print(a-b)
    elif choice==3:
        print(a*b)
    elif choice==4:
        print(a/b)
    else:
        print("Please enter a valid input from choices given")
    c=input("Do you wish to continue (yes/no) ?")
    if c.lower()!="yes":
        break




# We can use match also instead of if elif else
