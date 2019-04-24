# -*- coding: utf-8 -*-
# 博客地址
# http://www.cnblogs.com/alex3714/articles/5213184.html
# os.system()
# os.mkdir()
class Dog(object):
    name = "类变量"
    def __init__(self,name):
        self.name = name;

    # 类方法只能访问类变量，不能访问实例变量
    @classmethod
    def eatStatic(self):
        print ("%s is eating %s" %(self.name,'eatStatic'))

d = Dog("YUE")
d.eatStatic()
