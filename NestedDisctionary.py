# Nesting of dist into dist

# student_data={
#     "Ram":{"roll_no":21,"age":20,"course":"Python"},
#     "Shyam":{"roll_no":22,"age":30,"course":"Java"}
# }

# print(student_data)
# print(student_data["Ram"]["age"])
# student_data["Ram"]["phone_no"]=123456789
# # del student_data["Ram"]["phone_no"]
# val=student_data["Ram"].pop("phone_no")
# print(val)
# print(student_data)



# Nesting of list into disctionary

# travel_data ={

#     "Uttarakhand": ["Kedarnath","Badrinath","Devprayag" ,["Alaknanda","Bhagirathi"],"Dhari Devi"],
#     "Himanchal": ["Kasol","Manali","Shimla","Rohtang"]
# }

# print(travel_data)

# Nesting of disctionary into List

# travel_data ={

#     "Uttarakhand": [{"Kedarnath","Badrinath","Devprayag" , "River" , "Alaknanda","Dhari Devi"}],
#     "Himanchal": ["Kasol","Manali","Shimla","Rohtang"]
# }

# print(travel_data)

#Ad

Student_data =[
    {
        "Name":"Mohit",
        "roll_no":21,
        "age":25,
        "Course":"Python"
    },
    {
        "Name":"Rohit",
        "roll_no":25,
        "age":29,
        "Course":"Java"
    }

]

print(Student_data[1]["Name"])
def add_new_student(name,roll_no,age,course):
    new_studet={}
    new_studet["Name"]=name
    new_studet["roll_no"]=roll_no
    new_studet["age"]=age
    new_studet["Course"]=course

    Student_data.append(new_studet)
    print(Student_data)


add_new_student("Rohan",22,45,"C++")