from playwright.sync_api import Page
from utils.config import BASE_URL


class LoginPage:

    URL = BASE_URL

    def __init__(self, page: Page):
        self.page = page


    @property
    def txt_username(self):
        return self.page.locator("input[name='username']")


    @property
    def txt_password(self):
        return self.page.locator("input[name='password']")


    @property
    def btn_login(self):
        return self.page.locator("input[value='Log In']")
    


    def access_home(self):
        self.page.goto(self.URL)


    def fill_login(self, user, psw):
        self.txt_username.fill(user)
        self.txt_password.fill(psw)
        self.btn_login.click()