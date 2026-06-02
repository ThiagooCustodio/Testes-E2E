from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PesquisaPage(BasePage):

    CAMPO_PESQUISA = (
        By.ID,
        "js-h-search"
    )

    def pesquisar(self, texto):

        campo = self.find(self.CAMPO_PESQUISA)

        campo.send_keys(texto)
        campo.send_keys(Keys.ENTER)