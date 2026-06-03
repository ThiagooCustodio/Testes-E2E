from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_navegacao_mais_acessadas(driver):

    home = HomePage(driver)

    home.abrir()

    link_ver_mais = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.LINK_TEXT, "Ver mais")
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        link_ver_mais
    )

    titulo = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "h1.titleTop")
        )
    )

    assert titulo.text == "Mais acessados"
    assert "/mais-acessadas/" in driver.current_url
