from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://xeye-prod.ecxrnd.com")

    # Print page title
    print("Page Title:", page.title())

    browser.close()
