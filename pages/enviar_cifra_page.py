from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class EnviarCifraPage(BasePage):

    BTN_MAIS = (
        By.XPATH,
        "//span[contains(text(),'Mais')]"
    )

    BTN_ENVIAR = (
        By.XPATH,
        "//p[contains(text(),'Enviar cifra')]"
    )

    CAMPO_BUSCA = (
        By.ID,
        "input_search"
    )

    ARTISTA_LEGIAO = (
        By.XPATH,
        "//span[contains(text(),'Legião Urbana')]"
    )

    MUSICA_PAIS_FILHOS = (
        By.XPATH,
        "//b[contains(text(),'Pais e Filhos')]"
    )

    BTN_AVANCAR = (
        By.XPATH,
        "//button[contains(text(),'Avançar')]"
    )

    MSG_ERRO = (
        By.XPATH,
        "//h5[contains(text(),'Não conseguimos identificar nenhum acorde ou tablatura')]"
    )

    def abrir_envio(self):

        self.click(self.BTN_MAIS)
        self.click(self.BTN_ENVIAR)

    def selecionar_artista(self):

        self.write(
            self.CAMPO_BUSCA,
            "Legião Urbana"
        )

        self.click(self.ARTISTA_LEGIAO)

    def selecionar_musica(self):

        self.write(
            self.CAMPO_BUSCA,
            "Pais e Filhos"
        )

        self.click(self.MUSICA_PAIS_FILHOS)

    def avancar_todas_etapas(self):

        self.click(self.BTN_AVANCAR)
        self.click(self.BTN_AVANCAR)
        self.click(self.BTN_AVANCAR)

    def obter_mensagem_erro(self):

        return self.wait.until(
            EC.visibility_of_element_located(
                self.MSG_ERRO
            )
        ).text