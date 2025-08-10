class name:
    x = 0
    name = " "


    def __init__(self,z):
        self.name = z
        print("Hi", z)

class football_fans(name):
    points = 0

    def pts(self):
        print(self.name,"scores")

f = football_fans("AbhiCoder")
f.pts()





