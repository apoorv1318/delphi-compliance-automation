from playwright.sync_api import sync_playwright

def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Run in headful mode for debugging
        page = browser.new_page()

        # Open the login page
        page.goto("https://compliance.whyqtech.com/#/login")

        # Fill in the email field
        page.fill("[formcontrolname='email']", "test@gmail.com")

        # Fill in the password field
        page.fill("[formcontrolname='password']", "Kishan@1")

        # Click the Sign In button and wait for the page to load
        page.click("button[type='submit']")
        page.wait_for_url("https://compliance.whyqtech.com/#/admin/employee-list")

        # Verify successful login by checking URL
        assert page.url == "https://compliance.whyqtech.com/#/admin/employee-list"

        browser.close()


