class myClass:

    def __init__(self, name):
        self.x = 0
        self.n = name
        print (self.n, "Started")


    def my(self):
        self.x += 1
        print ('Used', self.x)

    def __del__(self):
        print ('I am Finished with', self.n, 'at', self.x)

class inherits(myClass):

    def __init__(self, name):
        super() .__init__(name)
        self.number = 1

    def count(self):
        self.number += 1
        self.my ()
        print (self.n, "counted", self.number)

a = myClass("A")
a.my()

b = inherits("B")
b.my()
b.count()

