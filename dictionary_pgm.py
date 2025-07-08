my_dict={"name":"Ebin","age":27,56:12,"hobbies":["Cycling","Coding",34,12]}

my_dict.update({"name":"Aswin"})
print(my_dict)

print(my_dict.pop("age"))
print(my_dict)
print(my_dict.popitem())
print(my_dict)

my_dict[7]="laptop"
print(my_dict)
print(my_dict[7])
print(my_dict.get(89,False))

print(my_dict)
my_dict.setdefault("language","Python")
print(my_dict)