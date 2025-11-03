class myClass:

    def __init__(self, z):
        self.x = 0
        self.name = z
        print (self.name, "Started")


    def cnt(self):
        self.x += 1
        print ('Used', self.x)

    def __del__(self):
        print ('I am Finished with', self.x)

s = myClass("alpha")
s.cnt()
j = myClass("beta")
j.cnt()

s.cnt()
j.cnt()
