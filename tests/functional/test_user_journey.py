from selenium.webdriver.common.by import By


def test_login_book_and_see_points(browser, live_server):
    # 1. Page d'accueil : on saisit l'email et on valide
    browser.get(live_server)
    browser.find_element(By.NAME, "email").send_keys("rich@test.com")
    browser.find_element(By.TAG_NAME, "button").click()
    assert "Welcome, rich@test.com" in browser.page_source

    # 2. On clique sur "Book Places" de Future Cup
    browser.find_element(By.CSS_SELECTOR, "a[href*='Future%20Cup']").click()

    # 3. On réserve 5 places
    browser.find_element(By.NAME, "places").send_keys("5")
    browser.find_element(By.TAG_NAME, "button").click()
    assert "Great-booking complete!" in browser.page_source
    assert "Points available: 25" in browser.page_source

    # 4. Le tableau public affiche les nouveaux points
    browser.get(live_server + "/points")
    assert "25" in browser.page_source