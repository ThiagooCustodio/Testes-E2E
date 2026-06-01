import time
from pages.home_page import HomePage
from pages.login_page import LoginPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_sucesso(driver):

    home = HomePage(driver)
    login = LoginPage(driver)

    home.abrir()

    home.acessar_login()

    login.login(
        "thiagorafaelcustodio@hotmail.com",
        "Qwaszx12345"
    )

    avatar = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "span[data-type='avatar']")
        )
    )

    avatar.click()

    # Aguarda aparecer a opção Sair
    logout = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//p[contains(text(),'Sair')]")
        )
    )

    assert logout.is_displayed()


#    perfil = WebDriverWait(driver, 20).until(
#        EC.element_to_be_clickable(
#            (By.CSS_SELECTOR, ".b3xqm ._voBV")
#        )
#    )

#    perfil.click()

#    logout = WebDriverWait(driver, 20).until(
#        EC.presence_of_element_located(
#            (By.ID, "logout")
#        )
#    )

#    assert logout.is_displayed()