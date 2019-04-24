# -*- coding: utf-8 -*-
# 博客地址
# http://www.cnblogs.com/alex3714/articles/5213184.html
from testPackage.C import C
class Dog(object):
    '''描述狗的'''
    # 构造函数
    def __init__(self,name):
        self.name = name
    def __call__(self, *args, **kwargs):
        print ("call方法")
    def __str__(self):
        return "<obj:%s>" %self.name
# obj = C()
# # 输出说明
# print (Dog.__doc__)
# # 输出模块
# print (obj.__module__)
# # 输出类
# print (obj.__class__)
# # __call__
# # 对象加()执行/类加()()
# Dog()(1,2)
# # 以字典形式打印调用者的内容
#
# # 打印类的所有属性
# print (Dog.__dict__)
# # 打印实例属性
# print (obj.__dict__)


#
# __str__
print (Dog("GG").__str__())

# 三个 __**item__ get/set/del
# 将类转为字典

# __new__


