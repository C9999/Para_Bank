from behave import given, when, then
from features.pages.login_page import LoginPage
from features.pages.transferencia_de_fundos_page import TransferPage
import random
from playwright.sync_api import expect

random_value = random.randint(2000, 2999)

@given('estou logado com um usuário válido')
def step_usuario_logado(context):
    context.execute_steps("""Quando eu inserir credenciais de login válidas""")


@when('eu realizar o fluxo de transferência de fundos')
def step_transfer_funds(context):
    context.transfer_page = TransferPage(context.page)
    context.page.get_by_role("link", name="Transfer Funds").click()
    context.transfer_page.fill_transfer_form(random_value)


@then('devo visualizar a mensagem de transferência realizado com sucesso')
def step_validated_transfer(context):
    expect(
        context.page.get_by_text("Transfer Complete!")
    ).to_be_visible()

@when('eu realizar o fluxo de transferência de fundos de forma inválida')
def step_transfer_funds_invalid(context):
    context.transfer_page = TransferPage(context.page)
    context.page.get_by_role("link", name="Transfer Funds").click()
    context.transfer_page.fill_transfer_form("error value")

@then('devo visualizar a mensagem informando que ocorreu um erro na transferência')
def step_validated_transfer_error(context):
    expect(
        context.page.get_by_text("An internal error has occurred and has been logged.")
    ).to_be_visible()