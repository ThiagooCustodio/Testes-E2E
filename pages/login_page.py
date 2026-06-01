from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    BTN_EMAIL = (
        By.XPATH,
        "//button[.//span[contains(text(),'Entrar com e-mail e senha')]]"
    )

    EMAIL = (
        By.CSS_SELECTOR,
        "[data-testid='email']"
    )

    SENHA = (
        By.CSS_SELECTOR,
        "[data-testid='password']"
    )

    BTN_ENTRAR = (
        By.CSS_SELECTOR,
        "button[type='submit']"
    )

    def abrir_login_email(self):

        botao = self.driver.find_element(*self.BTN_EMAIL)

        self.driver.execute_script(
            "arguments[0].click();",
            botao
        )

    def login(self, email, senha):
        
        print("Abrindo login por email")
        self.abrir_login_email()

        print("Preenchendo email")
        self.send_keys(self.EMAIL, email)

        print("Preenchendo senha")
        self.send_keys(self.SENHA, senha)

        print("Clicando em Entrar")
        self.click(self.BTN_ENTRAR)

        print("Login enviado")