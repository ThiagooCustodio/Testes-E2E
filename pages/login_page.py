from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL = (
        By.ID,
        "emailInput"
    )

    SENHA = (
        By.ID,
        "senhaInput"
    )

    BTN_ENTRAR = (
        By.NAME,
        "Entrar"
    )

    def login(self, email, senha):

        self.send_keys(
            self.EMAIL,
            email
        )

        self.send_keys(
            self.SENHA,
            senha
        )

        self.click(
            self.BTN_ENTRAR
        )