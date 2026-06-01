from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Abre Firefox
driver = webdriver.Firefox()

# Acessa o site
driver.get("https://www.estado.rs.gov.br/inicial")

# Procura o link Notícias e salva na variável
link_noticias = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.PARTIAL_LINK_TEXT, "Notícias")
    )
)

# Clica no link
link_noticias.click()

# Espera URL mudar
WebDriverWait(driver, 10).until(
    EC.url_contains("agencia-de-noticias")
)

# Mostra URL atual
print(driver.current_url)

# Verifica se navegou corretamente
assert "agencia-de-noticias" in driver.current_url

print("Teste passou!")

# Fecha navegador
driver.quit()