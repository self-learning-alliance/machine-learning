

def func(self):
    print("hahah")

# class Foo(object):
#
#     def __init__(self, name):
#         self.name = name
#
#
# f = Foo("alex")
#
# print(type(Foo))

# 对象后面有类，类有type

Foo = type('Foo',(),{'talk':func})

print(type(Foo))
f = Foo()
f.talk()
