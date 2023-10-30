from behave import *

calculator = {}

@given('I have entered the number {number} into the calculator')
def step_given(context, number):
    calculator['number'] = int(number)

@when('I press the {operation} button')
def step_when(context, operation):
    calculator['operation'] = operation

@when('I have entered another number {number} into the calculator')
def step_when_second_number(context, number):
    number = int(number)
    if calculator['operation'] == 'add':
        calculator['result'] = calculator['number'] + number
    elif calculator['operation'] == 'subtract':
        calculator['result'] = calculator['number'] - number

@then('the result displayed should be {result}')
def step_then(context, result):
    print(calculator)
    assert calculator['result'] == int(result), f"Expected {result}, but got {calculator['result']}"