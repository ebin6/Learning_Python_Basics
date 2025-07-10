my_list=[45,23,4,10,5,66,2]
print(set(enumerate(my_list,7)))
for c,k in enumerate(my_list,7):
    print(c,k)



print("")
for n in {45,23,5,2}:
    print(n,end=" ")
print("")
print("Iterating over Dictionary")
v={"name":"Ebin","age":27,2:45}
for k in v:
    print(k,v[k])
