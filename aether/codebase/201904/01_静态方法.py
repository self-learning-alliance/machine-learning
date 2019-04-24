# -*- coding: utf-8 -*-
# 博客地址
# http://www.cnblogs.com/alex3714/articles/5213184.html

# os.system()
# os.mkdir()
class Dog(object):
    def __init__(self,name):
        self.name = name;

    # @staticmethod
    def eat(self):
        print ("%s is eating %s" %(self.name,'dd'))
    # 切断与类的关联，只是一个单纯的函数
    @staticmethod
    def eatStatic():
        print ("%s is eating %s" %('YUE','eatStatic'))

    @staticmethod
    def eatStaticParam(self):
        print ("%s is eating %s" % (self.name, 'eatStaticParam'))

d = Dog("YUE")
d.eat()
d.eatStatic()
d.eatStaticParam(d)