"""Metin Dosyası İşlemleri"""
# file_name = input("Please enter a file name: ")

# with open(file_name, "r") as file:
#     data_list = [int(i) for i in file.readlines()]
#     print(f" Dosyadaki sayıların toplamı: {sum(data_list)}\
#           \n Dosyadaki sayıların ortalaması: {sum(data_list)/len(data_list):2f}")
    

    
"""Dosya Düzenleme"""

# file_name = input("Please enter a file name: ")


# with open(file_name, "r") as file:
#     lines = file.readlines()

# with open(file_name, "w") as file:
#     x = 1
#     for i in lines:
#         file.write(f"{x}: " + i)
#         x+=1
        
# with open(file_name, "r") as file:        
#     print(file.read())


""" JSON İşlemleri """ 

import json


def add_student(new_student, file_name="students.json"):
    with open(file_name, "r+", encoding="utf-8") as f:
        data = json.load(f)
        data["student_details"].append(new_student)
        f.seek(0)
        json.dump(data, f, indent=4)

def show_student(file_name="students.json"):
    with open(file_name, "r+", encoding="utf-8") as f:
        data = json.load(f)
        for i in data["student_details"]:
            print(i)

while True:
    your_choice = input("Enter a choice --> 'A' for 'Add'__'S' for 'Show'__'q' for 'Quit':  ").upper()    
    if your_choice == "A":
        new_student = {}
        s_name = input("Enter the name of the student: ")
        s_last_name = input("Enter the last name of the student: ")
        s_age = input("Enter the age of the student: ")
        new_student.update({"name": s_name, "last_name": s_last_name, "age": s_age})
        add_student(new_student)
        
    elif your_choice == "S":
        show_student()
        
    elif your_choice == "Q":
        break
    else:
        print("Please choose correctly!!")
