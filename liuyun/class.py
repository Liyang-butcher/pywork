class Person():
    mz = "李杨"
    age = 20

    def xxi(self):
        self.age = 17
        print("今天天气好")
    def fly(self):
        
        print("今天能上天吗？")

    def eat(self,food):
        self.wd = "好吃"
        print("我叫{}，今天吃了{}，味道{}{}".format(self.mz,food,self.wd))
p = Person()
print(p.mz,p.age)
p.xxi()
print(p.age)
p.fly()
p.eat("烧烤")
