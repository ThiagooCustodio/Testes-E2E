from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PesquisaPage(BasePage):

    CAMPO_PESQUISA = (
        By.ID,
        "js-h-search"
    )

    def pesquisar(self, musica):
        self.send_keys(
            self.CAMPO_PESQUISA,
            musica
        )