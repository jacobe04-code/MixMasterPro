from playwright.sync_api import sync_playwright

def verify_ui():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("file:///app/index.html")
        page.wait_for_timeout(2000)

        # 1. Check for Settings Button (Should be GONE)
        settings_btn = page.query_selector('button[title="Settings"]')
        if settings_btn:
            print("Settings button found (FAILED)")
        else:
            print("Settings button NOT found (PASSED)")

        # 2. Check for Reference Player Search Input (Should exist)
        search_input = page.query_selector('input[placeholder*="YouTube"]')
        if search_input:
            print("Search Input found (PASSED)")
        else:
            print("Search Input not found (FAILED)")

        browser.close()

if __name__ == "__main__":
    verify_ui()
