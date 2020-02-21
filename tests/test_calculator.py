from simple_calculator.calculator import Calculator

calculator = Calculator()


#Addition Testing
def test_add_two_numbers():
    assert calculator.add(1,2) == 3

def test_add_multiple_numbers():
    assert calculator.add(1,2,3,4,5) == 15

#Multiplication Testing
def test_multiply_two_numbers():
    assert calculator.multiplication(2,2) == 4

def test_multiply_multiple_numbers():
    assert calculator.multiplication(1,2,3) == 6
