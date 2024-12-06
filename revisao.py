#LER ENTRADAS DO USUÁRIO 
aluno = []
while True : # INFINITO 
     #lista que guardara todos os alunos  cadastrar 
    #ler a entrada do usuário 
    escolha_menu =int (input("escolha uma opção 1 cadastro: - 2 relatório: -3 para encerrar:")) #variavel que guarda qual opção do menu o úsario escolheu   
    if escolha_menu == 1: #se a escolha 
        situacao = ""
    
        cont = 0 # variavel que controla a repetição 
        escolha_usuario = int (input("Digite quantos alunos voce quer cadastrar:")) # variavel que guarda quantas vezes o codigo vai rodar
        while cont < escolha_usuario:
            nome = input("digite o nome do aluno:") #ARMAZENAR o nome do aluno 
            nota1 = float (input(" digite nota aluno:")) # 4 NOTAS DO ALUNO
            nota2 = float (input("digite nota aluno:"))
            nota3 = float (input("digite nota aluno:"))
            nota4 = float (input("digite nota aluno:"))

            faltas = int (input("faltas"))
            #calculo da media 
            media = (nota1+nota2+nota3+nota4)/4
            #logica da situacao 
            if faltas > 31:
                situacao = "reprovado por faltas"
            elif media >= 8:
                situacao = "aprovado"
            elif media >= 5:
                recuperacao = float (input("nota de recuperacao")) #LER A NOTA DA PROVA DE RECUPERACAO 
                if recuperacao >=(10-media):
                    situacao = "aprovado na recuperacao"
                else:
                    situacao = "reprovado na recuperacao"
            else: 
                situacao = "reprovado por media"
            #enviar os dados do aluno para a lista alunos 
            aluno.append([nome,faltas,media,situacao]) 
            cont += 1 
    elif escolha_menu == 2:  #relatorio
        print(aluno)
    elif escolha_menu == 3: #se o usuario escolheu 
        break # quebra a execução do enquanto 




















































