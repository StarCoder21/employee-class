class Employee:
    def __init__(self):
        print("employee created")

    def __del__(self):
        print("Destruction called")

def Create_obj():
    print("making object")
    obj= Employee()
    print("function end ")
    return obj
print("calling create_obj() function")
obj=Create_obj()
print('program end ')