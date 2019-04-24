# -*- coding: utf-8 -*-
# 使用场景，经过一些列的操作才能获取的一个状态（航班状态查询）
# 博客地址
# http://www.cnblogs.com/alex3714/articles/5213184.html
class Dog(object):
    def __init__(self,name):
        self.name = name
        self.__food = None

    # 属性方法：将方法作为静态属性
    @property
    def eatStatic(self):
        print ("%s is eating %s" %(self.name,self.__food))

    # 在属性方法下面，属性方法的赋值
    @eatStatic.setter
    def eatStatic(self,food):
        print ("%s is eating %s" % (self.name,food))
        self.__food = food

    @eatStatic.deleter
    def eatStatic(self):
        del self.__food
        print ("已删除")

d = Dog("YUE")
d.eatStatic
d.eatStatic = "property"

del d.eatStatic

d.eatStatic

# 属性方法的删除

