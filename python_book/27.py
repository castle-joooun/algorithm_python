from collections.abc import Sequence


class MyParentObject(object):
    def __init__(self):
        self.__private_field_123 = 71


class MyChildObject(MyParentObject):
    def get_private_field(self):
        return self.__private_field


baz = MyChildObject()
# baz.get_private_field()

print(baz._MyParentObject__private_field_123)
print(baz.__dict__)
