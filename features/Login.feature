# language: pt

Funcionalidade: Login

@smoke
Cenário: Login efetuado com sucesso
  Dado que acesso a página inicial do Parabank
  Quando eu inserir credenciais de login válidas
  Então devo ser visualizar a página de usuário logado

@regressão
Cenário: Login mal sucedido
  Dado que acesso a página inicial do Parabank
  Quando eu inserir credenciais de login inválidas
  Então devo visualizar a mensagem de erro ao tentar efetuar login
