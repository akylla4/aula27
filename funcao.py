#DECLARAR UMA FUNÇÃO 
def saudacoes (hora_do_dia): #exibir a saudação corresponde a hora 
#DAR BOM DIA
    if hora_do_dia >= 0 and (hora_do_dia <= 12) : 
        print ("bom dia!!!")
    elif (hora_do_dia >= 13) and (hora_do_dia <= 18) : 
        print ("boa tarde!")
    else:
        print("boa noite")
# FORA DA FUNÇÃO 
# peço para o usuário dizer a hora atual 
resposta = int (input("digite que horas sao:\n"))
#CHAMO A FUNÇÃO PASSANDO PARA ELA O PARAMETRO OBRIGATIVO 
saudacoes (resposta)

