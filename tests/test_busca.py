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

    resultado = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(
            (
                By.XPATH,
                "//*[contains(text(),'Resultados para')]"
            )
        )
    )

    assert 'Resultados para "legião urbana"' in resultado.text