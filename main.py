#cadastro de usuário e senha
saldo = 0.0 #variavel que guardara o saldo do usuario 
while True:
    #menu principal 
    print("bem vindo! /n digite 1.cadastrar 2.login 3.encerrar")
    #ler a escolha do usuário 

    escolha_menu = int (input())#lê a escolha como um numero inteiro 

    #se usuário escolher cadastro 
    if escolha_menu == 1:
        login_usuario = input("crie um nome de usuário")
        senha = input ("crie uma senha")
    elif escolha_menu == 2: #se usuário escolher login 
        #comparar as inf.cadastradas com umaq leitura 
        login_usuario = input ("dgite seu usuário")
        login_senha = input ("digite sua senha")
        if login_usuario == login_usuario and login_senha == senha : 
            print ("login realizado com sucesso")
            #se login correto, entra no 
            #menu principal do app
            while True : #enquanto que exibirá o menu principal
                 print ("1.deposito 2.sacar 3.extrato 4.encerrar")
                 escolha_principal = int (input())
                 if escolha_principal == 1 : 
                      #LÊ O VALOR A SER DEPOSITADO 
                      valor_deposito = float (input())
                      saldo = saldo + valor_deposito #atualizar o valor 
                 elif  escolha_principal == 2: #saque 
                      valor_saque = float (input("diite o valor do saque"))
                      senha_saque = input ("digite sua senha:")
                      if senha_saque == senha:
                           saldo = saldo - valor_saque #subtrai o valor do saldo  
                      else: 
                        print("sanha incorreta")
                 elif escolha_principal == 3:
                      valor_pix = float (input("digite o valor do pix"))
                      senha_pix = input ("digite sua senha")
                      if senha_pix == senha:
                           saldo = saldo - valor_pix
        else : 
            print ("USUÁRIO OU SENHA INCORRETOS")
    elif escolha_principal == 4: #se usuário escolher visualizar 
         senha_extrato=input("digite sua senha")
         if senha_extrato == senha:
             print("extato:",saldo)
         else: 
             print ("senha incorreta")
    elif escolha_principal == 5: #encerrar 
           senha_encerrar = input ("digite sua senha")
           if senha_encerrar == senha:
                break 
           else: 
                print ("senha incorreta")
    else:
         print("usuario ou senha incorretos")

