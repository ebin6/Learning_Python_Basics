try:
    with open("test_file3.txt",'r') as fileobject:
        fileobject.write("Kochi")
except FileNotFoundError:
    print("Please enter proper file path")