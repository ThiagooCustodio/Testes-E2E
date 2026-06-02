import time
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.enviar_cifra_page import EnviarCifraPage


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_mensagem_erro(driver):

    home = HomePage(driver)
    login = LoginPage(driver)
    enviar = EnviarCifraPage(driver)

    home.abrir()

    home.acessar_login()

    login.login(
        "thiagorafaelcustodio@hotmail.com",
        "Qwaszx12345"
    )

    enviar.abrir_envio()

    enviar.selecionar_artista()

    enviar.selecionar_musica()

    enviar.avancar_todas_etapas()

    mensagem = enviar.obter_mensagem_erro()

    assert (
        "não conseguimos identificar nenhum acorde ou tablatura"
        in mensagem.lower()
    )