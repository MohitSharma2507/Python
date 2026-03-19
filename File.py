
#? Summary 
# 'r' -> open for reading(default)
# 'w' -> open for writing,truncating the file first
# 'x' -> create a new file and open it for writing
# 'a' -> open for writing, appending to the end of the file if it exists
# 'b' -> binary mode
# 't' -> text mode(default)
# '+' -> open a disk file for updating(reading and writing )

#! Read a file

# with open("Error.txt", "r", encoding="utf-8") as f:
#     data = f.read()
#     print(data)
    
#!Write a file

# with open("Error.txt", "w", encoding="utf-8") as f:
#   f.write("This is another new line")
#   print(f)
    
#!append a file

with open("Error.txt", "a", encoding="utf-8") as f:
  f.write("\nAppended a new line")
  print(f)