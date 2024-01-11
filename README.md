## Automação de Cadastro de Produtos em Estoque

Este script em Python utiliza a biblioteca pyautogui para automatizar o processo de cadastro de produtos em um sistema de inventário. O processo é dividido em três passos principais:

#Passo 1: Login no Sistema
O script inicia abrindo o navegador Google Chrome e acessando a página de login do sistema da empresa. Ele preenche o e-mail e senha fornecidos, realizando o login no sistema.

#Passo 2: Importação da Base de Dados
A base de dados dos produtos é lida a partir de um arquivo CSV ("produtos.csv"). Certifique-se de que esse arquivo está localizado na área de trabalho e segue o formato esperado para uma importação correta.

#Passo 3: Cadastro de Produtos
O script itera sobre as linhas da base de dados e cadastra os produtos no sistema. Os detalhes do produto, como código, marca, tipo, categoria, preço unitário, custo e observações, são preenchidos nos campos apropriados do formulário.

#Nota Importante:
Este script é específico para um ambiente e pode necessitar de ajustes conforme as características do sistema alvo. Use com responsabilidade e de acordo com as políticas de automação da empresa.
