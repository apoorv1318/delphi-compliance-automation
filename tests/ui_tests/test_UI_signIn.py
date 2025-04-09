from playwright.sync_api import sync_playwright

LOGIN_URL = "https://compliance.whyqtech.com/#/login"

def test_signin_page_ui():
    """Test the UI elements of the Sign-In page"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set True for headless execution
        page = browser.new_page()

        # ✅ Navigate to the Login Page
        page.goto(LOGIN_URL)

        # ✅ Verify Page Title
        actual_title = page.title()
        print("Page Title:", actual_title)  # Debugging
        assert "Compliance" in actual_title, f"Expected title to contain 'Compliance', but got '{actual_title}'"

        # ✅ Check the Presence of UI Elements
        assert page.is_visible("text=Sign up"), "Sign-up text not visible"
        assert page.is_visible("text=Welcome back"), "Welcome message not visible"
        assert page.is_visible("[formcontrolname='email']"), "Email input field is missing"
        assert page.is_visible("[formcontrolname='password']"), "Password input field is missing"
        assert page.is_visible("button[type='submit']"), "Sign-in button is missing"
        assert page.is_visible("text=Forgot Password?"), "Forgot Password link is missing"

        # ✅ Verify Error Messages on Empty Submission
        page.click("button[type='submit']")
        assert page.is_visible("text=Email is required"), "Email validation message missing"
        assert page.is_visible("text=Password is required"), "Password validation message missing"

        print("✅ All UI elements are present and working correctly!")

        browser.close()
