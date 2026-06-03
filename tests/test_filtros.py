from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def clicar_js(driver, locator):
    elemento = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(locator)
    )

    driver.execute_script(
        "arguments[0].click();",
        elemento
    )


def test_filtro_violao_geral(driver):

    driver.get("https://www.cifraclub.com.br/mais-acessadas/")

    # Seleciona filtro de instrumento
    clicar_js(driver, (By.LINK_TEXT, "Todos os instrumentos"))
    clicar_js(driver, (By.LINK_TEXT, "Violão / Guitarra"))

    # Seleciona filtro de período
    clicar_js(driver, (By.LINK_TEXT, "Semanal"))
    clicar_js(driver, (By.LINK_TEXT, "Geral"))

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