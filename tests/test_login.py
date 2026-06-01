from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_login_sucesso(driver):

    home = HomePage(driver)
    login = LoginPage(driver)


    home.abrir()

    # Acessa a tela de login
    home.acessar_login()

    # Realiza o login
    login.login(
        "thiagorafaelcustodio@hotmail.com",
        "Qwaszx12345"
    )

    # Validação
    assert "Minha Conta" in driver.page_source