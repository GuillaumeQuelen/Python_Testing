import threading

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from werkzeug.serving import make_server

from server import app


@pytest.fixture
def live_server():
    """Lance le site sur le port 5001 pendant le test, puis l'arrête."""
    server = make_server("127.0.0.1", 5001, app)
    thread = threading.Thread(target=server.serve_forever)
    thread.start()
    yield "http://127.0.0.1:5001"
    server.shutdown()
    thread.join()


@pytest.fixture
def browser():
    """Ouvre Chrome, sans fenêtre visible (headless), puis le ferme."""
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
