from playwright.sync_api import sync_playwright

def test_empty_fields():
    """Test login with empty email and password fields"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Open login page
        page.goto("https://compliance.whyqtech.com/#/login")

        # Wait for the form fields to load
        page.wait_for_selector("[formcontrolname='email']")
        page.wait_for_selector("[formcontrolname='password']")

        # Click Sign In without entering anything
        page.click("button[type='submit']")

        # Debugging: Print all available error messages
        error_messages = page.locator("small.text-danger").all_text_contents()
        print("Found error messages:", error_messages)

        # Wait for both email and password error messages
        email_error = page.wait_for_selector("small.text-danger:has-text('Email is required')", timeout=10000)
        password_error = page.wait_for_selector("small.text-danger:has-text('Password is required')", timeout=10000)

        # Assertions to verify errors appear
        assert email_error.is_visible(), "Email error message is not displayed!"
        assert password_error.is_visible(), "Password error message is not displayed!"

        browser.close()
