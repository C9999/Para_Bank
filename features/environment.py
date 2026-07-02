import os

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()


def before_all(context):
    playwright = sync_playwright().start()

    headless = os.getenv("HEADLESS", "False").lower() == "true"
    slow_mo = int(os.getenv("SLOW_MO", "0"))

    browser = playwright.chromium.launch(
        headless=headless,
        slow_mo=slow_mo
    )

    context.playwright = playwright
    context.browser = browser


def before_scenario(context, scenario):
    context.page = context.browser.new_page()


def after_scenario(context, scenario):
    if scenario.status == "failed":
        os.makedirs("evidencias", exist_ok=True)

        file_name = "".join(
            c if c.isalnum() or c in (" ", "_", "-") else "_"
            for c in scenario.name
        ).replace(" ", "_")

        context.page.screenshot(
            path=f"evidencias/{file_name}.png",
            full_page=True
        )

    context.page.close()


def after_all(context):
    context.browser.close()
    context.playwright.stop()