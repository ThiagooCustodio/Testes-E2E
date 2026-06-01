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

    def abrir(self):
        self.driver.get(self.URL)

    def acessar_cadastro(self):
        self.click(self.BTN_CADASTRO)

    def acessar_login(self):

        botao = self.driver.find_element(*self.BTN_LOGIN)

        self.driver.execute_script(
            "arguments[0].click();",
            botao
        )