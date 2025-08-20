
# Example 9
class MyBaseClass(object):
    def __init__(self, value):
        self.value = value


class PlusTwoCorrect(MyBaseClass):
    def __init__(self, value):
        super(__class__, self).__init__(value)
        self.value += 2


class TimesFiveCorrect(MyBaseClass):
    def __init__(self, value):
        super(__class__, self).__init__(value)
        self.value *= 5


class GoodWay(TimesFiveCorrect, PlusTwoCorrect):
    def __init__(self, value):
        super(__class__, self).__init__(value)


print(GoodWay(5).value)
print(GoodWay.mro())
