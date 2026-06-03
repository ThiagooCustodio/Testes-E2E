from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):

    URL = "https://www.cifraclub.com.br/"

    BTN_CADASTRO = (
        By.CSS_SELECTOR,
        "._E9i2 > .hC0CP:nth-child(3) > ._5QAC"
    )

    BTN_LOGIN = (
        By.XPATH,
        "//button[.//span[contains(text(),'Entrar ou criar conta')]]"
    )

    BTN_MAIS = (
        By.CSS_SELECTOR,
        ".u-hideTabletDown:nth-child(2) li:nth-child(3)"
    )

    LINK_ENVIAR_CIFRA = (
        By.LINK_TEXT,
        "Enviar cifra"
    )

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 15)

    def abrir(self):
        self.driver.get(self.URL)

    def acessar_cadastro(self):
        self.click(self.BTN_CADASTRO)

    def acessar_login(self):
        botao = self.wait.until(
            EC.element_to_be_clickable(self.BTN_LOGIN)
        )
        self.driver.execute_script("arguments[0].click();", botao)

    def abrir_menu_mais(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BTN_MAIS)
        ).click()

    def ir_para_enviar_cifra(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LINK_ENVIAR_CIFRA)
        ).click()