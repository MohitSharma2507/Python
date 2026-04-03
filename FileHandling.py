import os

#? r = opens the file in read mode.The file handler exists at the beginning. It raises I/O error if the file doesn't exist
# file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close()

#! This automatically closes the file:
# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)

#?     It is default mode of opening files.

# file = open("file_2", "r")
# content = file.read()
# print(content)
# file.seek(0)  # 🔥 reset pointer

# print(f"Read One line {file.readline()}")  # reads one line
# file.seek(0) 
# print(f"Read All line {file.readlines()}")  # reads all lines as list

# file.close()

#? w = opens the file in write mode.It overwrites the file or create a new file if the file doesn't exist.The file handler exists at the beginning
# f1=open("file_1",'w')
# f1.write("Hey Mohit")

#? r+ = opens the file in both read and write mode.The file handler exists at the beginning, It raises I/O error if the file doesn't exist
# f1=open("file_1",'r+')
# # print(f1.read())
# f1.write("kaise ho")
# data = f1.read()
# print(data)
# # os.remove("file_1")

#? w+ = opens the file in both read and write mode.The file handler exists at the beginning. It overwrites the file or create a new file if the file doesn't exist

# f1=open("file_3",'w+')
# f1.write("how are you")

#? a = opens the file in append/write mode.The file handler exists at the end of the file if file already exist.If the file doesn't exist it will create a new file.
#?     The newly written data will be added at the end of the file.

# f1=open("file_3",'a')
# f1.write("how are you today")
# # print(f1.read())  #not readable
#?     The newly written data will be added at the end of the file.

# f1=open("file_3",'a+')
# f1.seek(0)
# # f1.write("how are you today")
# print(f1.read()) 


#! Binary File

with open("Mohit.png", "rb") as file:
    data = file.read()
