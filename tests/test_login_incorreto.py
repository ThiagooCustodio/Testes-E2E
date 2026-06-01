from pages.home_page import HomePage
from pages.login_page import LoginPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_incorreto(driver):

    home = HomePage(driver)
    login = LoginPage(driver)

    home.abrir()
    home.acessar_login()

    login.login(
        "aaa@gmail.com",
        "1234"
    )

    mensagem = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(
            (By.ID, "password-supportingText")
        )
    )

    assert mensagem.text == "E-mail ou senha inválidos"