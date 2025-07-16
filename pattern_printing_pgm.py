"""

*****
****
***
**
*

"""

"""
for k in range(5,0,-1):
    print("* "*k)
"""

"""for r in range(1,6):
       print(" "*int(5-r),"*"*r)
"""
"""print(list(range(5,0,-1)))"""

"""
1
2 4
3 6 9 
4 8 12 16
"""
for r in range(1,5):
    num=r
    for k in range(r):
        print(num,end=" ")
        num=num+r
    print()


for r in range(1,5):
    for k in range(1,r+1):
        print(r*k,end=" ")
    print()