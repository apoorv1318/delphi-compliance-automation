from playwright.sync_api import sync_playwright

def test_valid_email_wrong_password():

    """Test login with valid email and wrong password"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Open login page
        page.goto("https://compliance.whyqtech.com/#/login")

        # Enter valid email and wrong password
        page.fill("[formcontrolname='email']", "exampletest@gmail.com")
        page.fill("[formcontrolname='password']", "WrongPassword123")

        # Click Sign In
        page.click("button[type='submit']")

        # Wait for error message
        error_message = page.wait_for_selector("div.toast-message:has-text('Invalid email or password')", timeout=10000)

        # Assertion
        assert error_message.is_visible(), "Error message for wrong password is not displayed!"

        browser.close()
