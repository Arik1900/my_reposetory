from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.ebay.com/")
    search = page.locator("[id ='gh-ac']")
    search.type("Shirt")
    # page.keyboard.press("Enter")
    search_button = page.locator("[id ='gh-search-btn']")
    search_button.click()
    text = search_button.inner_text()
    search = page.locator("[name='search']")
    print(page.title())
    print(text)


    current_url = page.url
    print(current_url)
    page.close()
    browser.close()
    print("### Test end ###")