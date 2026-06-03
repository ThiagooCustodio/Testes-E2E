from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_filtro_violao_geral(driver):

    driver.get("https://www.cifraclub.com.br/mais-acessadas/")

    # Seleciona filtro de instrumento
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.LINK_TEXT, "Todos os instrumentos")
        )
    ).click()

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.LINK_TEXT, "Violão / Guitarra")
        )
    ).click()

    # Seleciona filtro de período
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.LINK_TEXT, "Semanal")
        )
    ).click()

    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.LINK_TEXT, "Geral")
        )
    ).click()

    # Captura os filtros aplicados
    instrumento = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "a.js-instrument-label")
        )
    )

    periodo = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "a.js-period-label")
        )
    )

    # Valida instrumento
    assert instrumento.text == "Violão / Guitarra"
    assert "on" in instrumento.get_attribute("class")

    # Valida período
    assert periodo.text == "Geral"
    assert "on" in periodo.get_attribute("class")