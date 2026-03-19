# student = dict({

#     "name": "Mohit Sharma",
#     "subjects" :{
#         "phy":98,
#         "chem":88,
#         "math":99
#     },
#     1:"modi"

# })


student = {

    "name": "Mohit Sharma",
    "subjects" :{
        "phy":98,
        "chem":88,
        "math":99
    },
    1:"modi"

}

student["name"] = "Rohit" # modify/update the value
student['gender'] = {"Male":4,"Female":43}  # modify/update the value
student["class" ] = 10 # modify/update the value
print(student)
print(list(student.keys()))

# Methods

print(f"Keys = {student.keys()}")  #returns all the keys
print(f"Values = {student.values()}") #returns all the values
print(f"All (Key,Values) = {student.items()}")#returns all [key,value] pairs as tuples
print(f"Specific values = {student.get("subjects")}") #returns the key according the values
# print(student.pop("class")) #remove and return the removed value
print(student.clear()) #clear the disctionary reutrn null
student1=student.copy() #clear the disctionary reutrn null
new_disc = {"phone":"7011******"}
student.update(new_disc) #inserts the specific items to the dictionary
print(student)