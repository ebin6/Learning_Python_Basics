a,b=map(int,input("Enter two numbers : ").split())
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Please enter a valid number greater than ")
except NameError:
    print("Value not defined for operants")

except Exception as e:
    print("Error",e)
else:
    print("No errors found")

