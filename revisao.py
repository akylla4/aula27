#LER ENTRADAS DO USUÁRIO 
nome = input() #ARMAZENAR o nome do aluno 
nota1 = float (input()) # 4 NOTAS DO ALUNO
nota2 = float (input())
nota3 = float (input())
nota4 = float (input())

faltas = int (input())
#calculo da media 
media = (nota1+nota2+nota3+nota4)/4

#logica da situacao 
if faltas > 31:
    situacao = "reprovado por faltas"
elif media >= 8:
    situacao = "aprovado"
elif media >= 5: "recuperacao"
recuperacao = float (input())#LER A NOTA DA PROVA DE RECUPERACAO
if recuperacao >=(10-media):
        situacao = "aprovado na recuperacao"
else:
     situacao = "reprovado na recuperacao"
else:
situacao = "reprovado por media"

#relatorio
print ("nome:",nome)
print ("notas",nota1,nota2,nota3,nota4)
print("faltas",faltas)
print("media",media)
print ('situacao',situacao) 
 






















































