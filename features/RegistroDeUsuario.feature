# language: pt

Funcionalidade: Registro de usuário

@smoke @regressão
Cenário: Registar novo usuário com sucesso
  Dado que acesso a página inicial do Parabank
  Quando eu preencher o formulário de registro com as informações obrigatórias
  E submeter o formulário
  Então devo ser visualizar a mensagem de registro realizado com sucesso

@regressão
Cenário: Erro ao registrar um usuário com informações incompletas
  Dado que acesso a página inicial do Parabank
  Quando eu preencher o formulário de registro com informações incompletas
  E submeter o formulário
  Então devo ser visualizar a mensagem informando que existem campos obrigatórios