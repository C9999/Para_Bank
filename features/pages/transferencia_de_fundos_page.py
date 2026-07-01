from playwright.sync_api import Page
import random

import random

accounts = [
    "12345",
    "12456",
    "12567",
    "12678",
    "12789",
    "12900",
    "13011",
    "13122",
    "13233",
    "13344",
    "13899",
    "54321"
]

from_account, destiny_account = random.sample(accounts, 2)

class TransferPage:

    def __init__(self, page: Page):
        self.page = page


    def fill_transfer_form(self, value):
        self.page.locator("#amount").fill(str(value))
        self.page.locator("#fromAccountId").select_option("13344")
        self.page.locator("#toAccountId").select_option("13344")
        self.page.get_by_role("button", name="Transfer").click()


    