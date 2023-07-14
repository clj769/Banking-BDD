from behave import given, when, then
from src.bank import BankAccount

@given(u'a bank account with balance of {initial_balance:d}')
@given('a bank account with initial balance of {initial_balance:d}')
def step_given_initial_balance(context, initial_balance):
    context.account = BankAccount(initial_balance)
    context.account.balance = initial_balance

@when('we deposit {deposit_amount:d} pounds into the account')
def step_when_deposit(context, deposit_amount):
    context.account.deposit(deposit_amount)

@when('we withdraw {withdraw_amount:d} pounds from the account')
def step_when_withdraw(context, withdraw_amount):
    context.account.withdraw(withdraw_amount)

@then('the balance should be {expected_balance:d}')
def step_then_check_balance(context, expected_balance):
    assert context.account.balance == expected_balance