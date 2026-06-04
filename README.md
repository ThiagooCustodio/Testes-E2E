# Testes E2E - Cifra Club

Projeto de automação de testes End-to-End (E2E) desenvolvido com Python, Selenium WebDriver e Pytest, utilizando o padrão Page Object Model (POM).

## Objetivo

Automatizar cenários reais de navegação e interação no site Cifra Club, validando funcionalidades importantes da aplicação sob a perspectiva do usuário final.

## Tecnologias Utilizadas

Python 3.14
Selenium WebDriver
Pytest
Firefox WebDriver (GeckoDriver)
Page Object Model (POM)
Git e GitHub

## Estrutura do Projeto

Trabalho teste E2E
├── pages/
│   ├── base_page.py
│   ├── cadastro_page.py
│   ├── profile_page.py
│   ├── pesquisa_page.py
│   ├── home_page.py
│   ├── login_page.py
│   └── enviar_cifra_page.py
│
├── tests/
│   ├── test_busca.py
│   ├── test_login.py
│   ├── test_mensagem_erro.py
│   ├── test_navegacao.py
│   └── test_filtros.py
│
├── conftest.py
├── requirements.txt
└── README.md

## Cenários Automatizados

### Busca de cifras

Valida a funcionalidade de busca do site, verificando se os resultados são apresentados corretamente ao usuário.

### Login

Teste realiza o Login com credenciais inválidas

Valida a exibição da mensagem:

"E-mail ou senha inválidos"


teste Login com credenciais válidas

Valida o acesso do usuário e a exibição do menu de conta através do avatar do perfil.


### Navegação entre páginas


Valida a navegação da página inicial para a seção "Mais acessados"


Confirmando que o título correto da página foi carregado.


### Filtros da página Mais Acessados

Valida a aplicação dos filtros:

* Instrumento: Violão / Guitarra
* Período: Geral

Confirmando que os filtros foram aplicados.


### Envio de cifra com validação de erro


Realiza o fluxo maior:

1. Login no sistema.
2. Acesso à funcionalidade Enviar Cifra.
3. Seleção de artista.
4. Seleção de música.
5. Navegação pelas etapas do formulário.
6. Validação da mensagem de erro apresentada pelo sistema.

Mensagem validada:

Não conseguimos identificar nenhum acorde ou tablatura

## Como Executar
### Instalar dependências

pip install -r requirements.txt

### Executar todos os testes

pytest

### Executar um teste específico

```bash
pytest tests/test_login.py
```

### Executar com detalhes

pytest -v

## Boas Práticas Aplicadas

* Utilização do padrão Page Object Model.
* Reutilização de código através de classes de páginas.
* Uso de WebDriverWait para sincronização.
* Separação entre lógica de teste e elementos da interface.
* Automação de cenários positivos e negativos.
* Organização da suíte de testes para facilitar manutenção e evolução.

## Repositório

Projeto desenvolvido para estudos e prática de automação de testes E2E utilizando Selenium e Pytest.
