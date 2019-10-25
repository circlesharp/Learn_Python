## 老鼠书_第31章
## pizzashop.py
## OOP和组合：“has-a”关系
"""
组合：内嵌对象集合体
组合类一般都提供自己的接口，并通过内嵌的对象来实现接口。
"""

from employees import PizzaRobot, Server

class Customer:
    def __init__(self, name):
        self.name = name
    def order(self, server):
        print(self.name, "orders from", server)
    def pay(self, server):
        print(self.name, "pays for item to", server)

class Oven:
    def bake(self):
        print("oven bakes")

class PizzaShop:
    def __init__(self):
        self.server = Server('Pat')  # 服务员叫 Pat
        self.chef = PizzaRobot('Bob')  # 机器人叫 Bob
        self.oven = Oven()
    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

if __name__ == "__main__":
    scene = PizzaShop()
    scene.order('Homer')  # 每一次 order 都产生一个 customer 对象
    print('...')
    scene.order('Shaggy')