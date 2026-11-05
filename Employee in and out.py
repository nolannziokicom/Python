class emlpoyee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Program ended")

def create_obj():
    print("making object")
    obj=emlpoyee()

    print("Function end")
    return obj

print("Calling create obj function...")

obj=create_obj()
print("Destructor called")


