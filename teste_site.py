from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Abre Firefox
driver = webdriver.Firefox()


# Acessa o site
driver.get("https://www.estado.rs.gov.br/inicial")

# Espera o body carregar
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "body"))
)


# Verifica se carregou
assert "Rio Grande do Sul" in driver.page_source


driver.quit()