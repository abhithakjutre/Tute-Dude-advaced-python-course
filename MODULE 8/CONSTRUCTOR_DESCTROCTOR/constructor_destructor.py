class const_dest:
    x = 0
    def __init__(self): # This is constructor

        print("Welcome!")

    def __del__(self): # This is destructor
        print("Thank you sir")

    def add(self,a,b):
        self.a = a
        self.b = b
        return a * b

cd = const_dest()
print("Your add result is: ",cd.add(5,6))
