import time
from pages.home_page import HomePage
from pages.pesquisa_page import PesquisaPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_pesquisar_artista(driver):

    home = HomePage(driver)
    pesquisa = PesquisaPage(driver)

    home.abrir()

    pesquisa.pesquisar("legião urbana")

    time.sleep(5)
    
    assert "legião urbana" in driver.page_source.lower()