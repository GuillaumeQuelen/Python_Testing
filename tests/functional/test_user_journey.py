from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def wait_for_text(browser, text, timeout=10):
    """Attend que le texte apparaisse dans la page (10 s maximum)."""
    WebDriverWait(browser, timeout).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "body"), text)
    )


def test_login_book_and_see_points(browser, live_server):
    # 1. Page d'accueil : on saisit l'email et on valide
    browser.get(live_server)
    browser.find_element(By.NAME, "email").send_keys("rich@test.com")
    browser.find_element(By.TAG_NAME, "button").click()
    wait_for_text(browser, "Welcome, rich@test.com")

    # 2. On clique sur "Book Places" de Future Cup
    browser.find_element(By.CSS_SELECTOR, "a[href*='Future%20Cup']").click()
    wait_for_text(browser, "Places available")

    # 3. On réserve 5 places
    browser.find_element(By.NAME, "places").send_keys("5")
    browser.find_element(By.TAG_NAME, "button").click()
    wait_for_text(browser, "Great-booking complete!")
    assert "Points available: 25" in browser.page_source

    # 4. Le tableau public affiche les nouveaux points
    browser.get(live_server + "/points")
    wait_for_text(browser, "Points of each club")
    assert "25" in browser.page_source