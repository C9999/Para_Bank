# ParaBank - Framework de Automação de Testes

## Sobre o projeto

Este projeto consiste em um framework de automação de testes E2E desenvolvido para a aplicação ParaBank, utilizando Python, Playwright e Behave (BDD).

---

# Tecnologias utilizadas

* Python 3.13+
* Playwright
* Behave (BDD)
* Allure Report
* Git

---

# Estrutura do projeto

```text
Para_Bank/
│
├── features/
│   ├── pages/
│   │   ├── common_page.py
│   │   ├── login_page.py
│   │   ├── registro_de_usuario_page.py
│   │   ├── transferencia_de_fundos_page.py
│   │
│   ├── steps/
│   │   ├── common_steps.py
│   │   ├── login_steps.py
│   │   ├── registro_de_usuario_steps.py
│   │   ├── transferencia_de_fundos_steps.py
│   │
│   ├── environment.py
│   │
│   ├── Login.feature
│   ├── RegistroDeUsuario.feature
│   ├── TransferenciaDeFundos.feature
│
├── allure-results/
├── allure-report/
├── to-do-other-tests/
│   ├── backend/
│   ├── k6/
│   └── visual-regression/
│
├── .env
├── requirements.txt
└── README.md
```

---

# Organização de pastas e arquivos

## features/pages

Contém as Page Objects responsáveis por guardar todas os elementos e funções usadas nas interações com o FrontEnd.

## features/steps

Contém a implementação dos Steps descridos no Behave(BDD). E cada Step possui a responsabilidade de organizar as ações da automação, e deixando a responsabilidade de interação com a aplicação para as Pages.

## Features

Os arquivos `.feature` descrevem os cenários, tornando os testes mais legíveis e próximos da linguagem de negócio.

Exemplo:

```gherkin
Funcionalidade: Login

Cenário: Login efetuado com sucesso

Dado que acesso a página inicial do Parabank
Quando eu inserir credenciais de login válidas
Então devo visualizar a página de usuário logado
```

# Instalação do projeto

## Clonar o repositório

```bash
git clone <URL_DO_REPOSITORIO>

cd Para_Bank
```

---

## Criar ambiente virtual

Windows

```bash
python -m venv .venv
```

Ativar:

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Instalar as dependências

```bash
pip install -r requirements.txt
```

---

## Instalar os navegadores do Playwright

```bash
playwright install
```

---

## Instalar o Allure

Caso ainda não possua instalado:

```bash
scoop install allure
```

ou

```bash
choco install allure-commandline
```

---

# Executando os testes

## Executar todos os testes

```bash
behave
```

---

## Executar uma Feature específica

Login

```bash
behave features/Login.feature
```

Registro de Usuário

```bash
behave features/RegistroDeUsuario.feature
```

Transferência de Fundos

```bash
behave features/TransferenciaDeFundos.feature
```

---

## Executar um cenário específico

```bash
behave features/Login.feature --name "Login efetuado com sucesso"
```

---

# Relatórios Allure

## Executar todos os testes gerando os resultados

```bash
behave -f allure_behave.formatter:AllureFormatter -o allure-results
```

---

## Abrir o relatório

```bash
allure serve allure-results
```

---

## Gerar relatório HTML

```bash
allure generate allure-results --clean -o allure-report
```

Abrir o relatório:

```bash
allure open allure-report
```

---

# Padrões aplicados

* Page Object Model (POM)
* Separação entre Features, Steps e Pages
* Utilização de variáveis de ambiente
* Reutilização de componentes
* Estrutura preparada para integração contínua (CI/CD)
* Relatórios de execução utilizando Allure
* Geração dinâmica de dados para execução dos testes

---

# To-do

`to-do-other-tests/`

Os próximos objetivos são:

* Criar arquivo centralizado com os dados de login.
* Integrar com pipeline CI/CD.
* Validar contratos, códigos de resposta e regras de negócio.
* Integrar os testes de API ao pipeline de execução.
* Desenvolver cenários utilizando K6.
* Criar testes de carga.
* Criar testes de estresse.
* Gerar métricas e relatórios de desempenho.
* Implementar comparação automática de screenshots.
* Detectar alterações visuais entre versões da aplicação.
* Integrar a validação visual ao pipeline de testes.
