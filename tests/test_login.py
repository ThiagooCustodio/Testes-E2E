import time
from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_login_sucesso(driver):

    home = HomePage(driver)
    login = LoginPage(driver)

    home.abrir()

    home.acessar_login()

    login.login(
        "thiagorafaelcustodio@hotmail.com",
        "Qwaszx12345"
    )

