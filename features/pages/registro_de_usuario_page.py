from playwright.sync_api import Page
import random


class RegisterPage:

    def __init__(self, page: Page):
        self.page = page


    def access_home(self):
        self.page.goto(self.URL)


    def fill_form(self, name, last_name, address, city, state, zip_code, ssn):
        self.page.locator("input[name='customer.firstName']").fill(name)
        self.page.locator("input[name='customer.lastName']").fill(last_name)
        self.page.locator("input[name='customer.address.street']").fill(address)
        self.page.locator("input[name='customer.address.city']").fill(city)
        self.page.locator("input[name='customer.address.state']").fill(state)
        self.page.locator("input[name='customer.address.zipCode']").fill(zip_code)
        self.page.locator("input[name='customer.ssn']").fill(ssn)
        self.create_user_name()
            

    def create_user_name(self):
        random_id = random.randint(100, 999) 
        self.page.locator("input[name='customer.username']").fill(f"carlos_parabank_{random_id}")
        self.page.locator("input[name='customer.password']").fill("123456")
        self.page.locator("#repeatedPassword").fill("123456")

    def fill_form_incomplete(self, name):
        self.page.locator("input[name='customer.firstName']").fill(name)
        
