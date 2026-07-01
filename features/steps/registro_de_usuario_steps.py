from behave import given, when, then
from features.pages.login_page import LoginPage
from features.pages.registro_de_usuario_page import RegisterPage
from playwright.sync_api import expect


@when('eu preencher o formulário de registro com as informações obrigatórias')
def step_fill_register(context):
    context.register_page = RegisterPage(context.page)

    context.page.get_by_role("link", name="Register").click()
    context.register_page.fill_form("Carlos", "Araújo", "Avenida Paulista 500", "São Paulo", "SP", "01310-100", "078-05-1120")

@when('submeter o formulário')
def step_submit_form(context):
    context.page.get_by_role("button", name="Register").click()


@then('devo ser visualizar a mensagem de registro realizado com sucesso')
def step_validated_register(context):
    expect(context.page.get_by_text
           ("Your account was created successfully. You are now logged in.")
    ).to_be_visible()


@when('eu preencher o formulário de registro com informações incompletas')
def step_fill_incomplete_register(context):
    context.register_page = RegisterPage(context.page)

    context.page.get_by_role("link", name="Register").click()
    context.register_page.fill_form_incomplete("Mônica")


@then('devo ser visualizar a mensagem informando que existem campos obrigatórios')
def step_validated_incomplete_register(context):
    expect(context.page.get_by_text("Social Security Number is")).to_be_visible()