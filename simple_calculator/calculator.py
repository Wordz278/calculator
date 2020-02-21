class Calculator:

    def __init__(self):
        pass

    def add(self, *args):
        sum = 0
        for val in args:
            num = int(val)
            sum += num
        return sum

    def multiplication(self, *args):
        product = 1
        for val in args:
            num = int(val)
            product *= num
        return product

