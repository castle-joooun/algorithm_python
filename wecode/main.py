# absoulte path
#from calculator.add_and_multiply import add_and_multiply


# relative path
from .calculator.add_and_multiply import add_and_multiply


if __name__ == '__main__':
    print(add_and_multiply(1,2))