## 老鼠书_第30章
## private0.py
## 实现属性私有化，不允许在类外部对某些属性进行修改

class PrivateExc(Exception): pass

class Privacy:
    def __setattr__(self, attrname, value):
        if attrname in self.privates:  # 抽象类，privates是子类的属性，是一个列表
            raise PrivateExc(attrname, self)
        else:
            self.__dict__[attrname] = value

class Test1(Privacy):
    privates = ['age']

class Test2(Privacy):
    privates = ['name', 'pay']
    def __init__(self):
        self.__dict__['name'] = 'Tom'

if __name__ == '__main__':
    x = Test1()
    y = Test2()

    x.name = "Bob"
    # y.name = "Sue"
    print(x.name)

    y.age = 30
    # x.age = 40
    print(y.age)