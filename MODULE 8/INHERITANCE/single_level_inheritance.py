# This is example of single level inheritance
class A:

    def state_1(self):
        print("State_1 present")
    def state_2(self):
        print("State_2 present")
    def state_3(self):
        print("State_3 present")

class B(A):
    def state_4(self):
        print("State_4 present")
    def state_5(self):
        print("State_5 present")


b = B()
b.state_1()
b.state_2()
b.state_3()
b.state_4()
b.state_5()



