from behave import given, when, then
from Calculator import *


@given('I have entered {number_f_1:f} into the calculator')
def enter_number1_f(context, number_f_1):
    context.number_f_1 = number_f_1


@given('I have also entered {number2:f} into the calculator')
def enter_number2_f(context, number_f_2):
    context.number_f_2 = number_f_2


@when('I press {action:w}')
def press_action(context, action):
    # context.calculator = Calculator()
    # context.result = addition(context.number1, context.number2)
    context.action = action
    if action == "plus":
        context.result = result("+", context.number_f_1, context.number_f_2)
    elif action == "minus":
        context.result = result("-", context.number_f_1, context.number_f_2)
    elif action == "multiply":
        context.result = result("*", context.number1, context.number2)
    elif action == "div":
        context.result = result("/", context.number1, context.number2)


@then('the {result:f} should be on the screen')
def check_result_f(context, result):
    assert context.result == result
