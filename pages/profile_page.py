from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProfilePage(BasePage):

    MENU_PERFIL = (
        By.CSS_SELECTOR,
        ".b3xqm ._voBV"
    )

    BTN_LOGOUT = (
        By.ID,
        "logout"
    )

    def abrir_menu(self):
        self.click(self.MENU_PERFIL)

    def logout_visivel(self):
        return self.driver.find_element(*self.BTN_LOGOUT).is_displayed()