## 老鼠书_第31章
## employees.py
## OOP和继承：“is-a”关系 => “is-a”链 机器人 is a 主厨，主厨 is a 员工。

class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary
    def giveRaise(self, percent):
        self.salary = self.salary + (self.salary * percent)
    def work(self):
        print(self.name, "does stuff")
    def __repr__(self):
        return "<Employee: name=%s, salary=%s>" % (self.name, self.salary)

class Chef(Employee):
    def __init__(self, name):  # 直接调用父类的 __init__
        Employee.__init__(self, name, 50000)
    def work(self):  # 覆盖父类的 work
        print(self.name, "make food")

class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 40000)
    def work(self):
        print(self.name, "interfaces with customer")

class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)  # 尽管这里没写工资，但是 Chef 类已经规定为 50000 了
    def work(self):
        print(self.name, "makes pizza")

if __name__ == "__main__":
    bob = PizzaRobot('bob')
    print(bob)
    bob.work()
    bob.giveRaise(.2)
    print(bob); print()

    for klass in Employee, Chef, Server, PizzaRobot:
        obj = klass(klass.__name__)  # 类.__name__ 得到的是这个类的名字
        obj.work()