# language: pt

Funcionalidade: Transferência de fundos

@smoke @regressão
Cenário: Transferir fundos para outra conta
  Dado que acesso a página inicial do Parabank
  E estou logado com um usuário válido
  Quando eu realizar o fluxo de transferência de fundos
  Então devo visualizar a mensagem de transferência realizado com sucesso

@regressão
Cenário: Erro ao transferir valores inválidos
  Dado que acesso a página inicial do Parabank
  E estou logado com um usuário válido
  Quando eu realizar o fluxo de transferência de fundos de forma inválida
  Então devo visualizar a mensagem informando que ocorreu um erro na transferência
