class Cat():
    def __init__(self,foog):
        self.a = foog
    def add(self):
        self.d = 1
       

c = Cat("xixi")
print(c.a)
c.add()
print(c.d)
