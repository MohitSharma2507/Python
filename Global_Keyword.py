def display():
    a=20
    def show():
        global a
        a=30
        print("Inside show() function a =",a)
    print("Before calling show() function a =",a)
    show()
    print("After calling show() function a =",a)
display()
print("Value of a outside the function =",a)    