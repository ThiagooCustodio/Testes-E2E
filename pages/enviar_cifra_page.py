import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage


class EnviarCifraPage(BasePage):

    BTN_CIFRAS = (By.CSS_SELECTOR, "rect:nth-child(7)")
    CAMPO_BUSCA = (By.ID, "input_search")
    BTN_AVANCAR = (By.XPATH, "//button[contains(text(),'Avançar')]")
    MSG_ERRO = (
        By.XPATH,
        "//h5[contains(text(),'Não conseguimos identificar nenhum acorde ou tablatura')]"
    )

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 15)

    def selecionar_tipo_cifra(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BTN_CIFRAS)
        ).click()

    def _digitar_devagar(self, campo, texto):
        campo.clear()
        for letra in texto:
            campo.send_keys(letra)
            time.sleep(0.2)
        time.sleep(3)  # aguarda dropdown carregar

    def _clicar_primeira_sugestao(self):
        campo = self.driver.find_element(*self.CAMPO_BUSCA)
        time.sleep(2)                    # aguarda dropdown aparecer
        campo.send_keys(Keys.ARROW_DOWN) # seleciona primeiro item
        time.sleep(0.5)
        campo.send_keys(Keys.RETURN)     # confirma a seleção
        time.sleep(1)                    # aguarda a página processar

    def selecionar_artista(self):
        campo = self.wait.until(
            EC.element_to_be_clickable(self.CAMPO_BUSCA)
        )
        self._digitar_devagar(campo, "Legião Urba")
        self._clicar_primeira_sugestao()

    def selecionar_musica(self):
        campo = self.wait.until(
            EC.element_to_be_clickable(self.CAMPO_BUSCA)
        )
        self._digitar_devagar(campo, "Pais e Filhos")
        self._clicar_primeira_sugestao()

    def avancar_todas_etapas(self):
        for _ in range(3):
            botao = self.wait.until(
                EC.element_to_be_clickable(self.BTN_AVANCAR)
            )
            self.driver.execute_script("arguments[0].click();", botao)
            time.sleep(2)
            
    def obter_mensagem_erro(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.MSG_ERRO)
        ).text