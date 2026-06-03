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
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".u-hideTabletDown"))
    )

    WebDriverWait(driver, 15).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "modalOverlay"))
    )

    mais = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Mais')]/ancestor::li"))
)
    driver.execute_script("arguments[0].click();", mais)

    home.abrir_menu_mais()
    home.ir_para_enviar_cifra()

    enviar.selecionar_artista()
    enviar.selecionar_musica()
    enviar.avancar_todas_etapas()

    mensagem = enviar.obter_mensagem_erro()

    assert "não conseguimos identificar nenhum acorde ou tablatura" in mensagem.lower()