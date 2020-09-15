a = 18
class baba():
    
    def sr(self):
        a = 20
        print(a)
        print("我儿奉先")
class son(baba):
    def add(self,food):
        print("今天吃的{}".format(food))
p = son()
p.sr()
p.add("海鲜")
print(a)

