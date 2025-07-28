import copy

my_list=[[23,12,4],["Ebin","Python"]]

g=copy.deepcopy(my_list)

g[0][1]='ABC'

print(g)
print(my_list)