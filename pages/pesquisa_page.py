from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class PesquisaPage(BasePage):

    CAMPO_PESQUISA = (
        By.CSS_SELECTOR,
        'input[type="search"]'
    )

    def pesquisar(self, termo):
        campo = self.find(self.CAMPO_PESQUISA)
        campo.clear()
        campo.send_keys(termo)
        campo.send_keys(Keys.ENTER)