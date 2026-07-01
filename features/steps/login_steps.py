from behave import given, when, then
from features.pages.login_page import LoginPage
from playwright.sync_api import expect


@when('eu inserir credenciais de login válidas')
def step_login(context):
    context.login_page.fill_login("john", "demo")


@then('devo ser visualizar a página de usuário logado')
def step_validated_login(context):
    expect(
        context.page.get_by_role("heading", name="Accounts Overview")
    ).to_be_visible()


@when('eu inserir credenciais de login inválidas')
def step_login(context):
    context.login_page.fill_login("hacker", "")


@then('devo visualizar a mensagem de erro ao tentar efetuar login')
def step_validated_login(context):
    expect(
        context.page.get_by_text("Please enter a username and password.")
    ).to_be_visible()
