from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CadastroPage(BasePage):

    NOME = (By.ID, "fullName")
    EMAIL = (By.ID, "email")
    SENHA = (By.ID, "password")
    CONFIRMAR_SENHA = (By.ID, "repeatPassword")

    CHECK_TERMOS = (
        By.ID,
        "usage-terms"
    )

    BTN_ENVIAR = (
        By.NAME,
        "Enviar cadastro"
    )

    def preencher_nome(self, nome):
        self.send_keys(self.NOME, nome)

    def preencher_email(self, email):
        self.send_keys(self.EMAIL, email)

    def preencher_senha(self, senha):
        self.send_keys(self.SENHA, senha)

    def confirmar_senha(self, senha):
        self.send_keys(self.CONFIRMAR_SENHA, senha)

    def aceitar_termos(self):
        self.click(self.CHECK_TERMOS)

    def enviar(self):
        self.click(self.BTN_ENVIAR)

    def cadastrar(
        self,
        nome,
        email,
        senha,
        confirmar
    ):
        self.preencher_nome(nome)
        self.preencher_email(email)
        self.preencher_senha(senha)
        self.confirmar_senha(confirmar)
        self.aceitar_termos()
        self.enviar()