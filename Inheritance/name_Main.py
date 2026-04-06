# Every Python file has a special built-in variable called __name__.

# When you run a file directly, Python sets:
# __name__ = "__main__"

# When you import that file as a module, Python sets:
# __name__ = "filename"

# It ensures that some code runs only when the file is executed directly, and does NOT run when the file is imported.\

def greet():
    print("Hello!")

if __name__ == "__main__":
    print("This file is running directly")
    greet() 