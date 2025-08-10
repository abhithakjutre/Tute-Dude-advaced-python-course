class sample:

    def __init__(self):
        self.value_1 = 1
        self.value_2 = 2

    def __A1_(self): # This function is hide
        print("apple")

    def __B2_(self):
        print("ball")

s = sample()
# s.__A1_()  you can't access this function
print(dir(s)) # Access first step is this now run and find 'A1' in dir
s._sample__A1_() # now you access this function

# This is data hiding
