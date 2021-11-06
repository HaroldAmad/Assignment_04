def getuserInput ():
    name_F = input("Name: ")
    age_F = int(input("Age: "))
    add_F = input("Address: ")
    return name_F, age_F, add_F

def display(nameFunc, ageFunc, addFunc):
    print(f"Hi, my name is {nameFunc}. I {ageFunc} years old and I live in {addFunc}.")

name, age, add = getuserInput