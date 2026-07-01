from behave import given
from features.pages.login_page import LoginPage


@given('que acesso a página inicial do Parabank')
def step_access_parabank(context):
    context.login_page = LoginPage(context.page)
    context.login_page.access_home()