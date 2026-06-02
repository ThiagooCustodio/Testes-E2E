from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProfilePage(BasePage):

    AVATAR = (
        By.CSS_SELECTOR,
        "span[data-type='avatar']"
    )

    BTN_SAIR = (
        By.XPATH,
        "//p[contains(text(),'Sair')]"
    )

    def abrir_menu(self):
        self.click(self.AVATAR)

    def sair_visivel(self):
        return self.find(self.BTN_SAIR).is_displayed()