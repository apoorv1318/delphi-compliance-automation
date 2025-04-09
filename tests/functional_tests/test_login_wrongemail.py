from playwright.sync_api import sync_playwright


def test_wrong_email_valid_password():


    """Test login with wrong email and valid password"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Open login page
        page.goto("https://compliance.whyqtech.com/#/login")

        # Enter wrong email and valid password
        page.fill("[formcontrolname='email']", "wrongemail@example.com")
        page.fill("[formcontrolname='password']", "********")

        # Click Sign In
        page.click("button[type='submit']")

        # Wait for error message
        error_message = page.wait_for_selector("div.toast-message:has-text('Failed to findByEmail')", timeout=10000)

        # Assertion
        assert error_message.is_visible(), "Error message for wrong email is not displayed!"

        browser.close()
