
class Person(object):
    def __init__(self,name):
        self.name = name

    def eat(self):
        print("%s is eating..."%self.name)

d = Person("岳梁")
# 根据输入选择方法执行
choice = input(">>:").strip()

if(hasattr(d,choice)):

    print(getattr(d,choice)())

# hasattr
# getattr
#

