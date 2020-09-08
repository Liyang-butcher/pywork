class baba():
    def sr(self):
        print("我儿奉先")
class son(baba):
    def add(self,food):
        print("今天吃的{}".format(food))
p = son()
p.sr()
p.add("海鲜")


