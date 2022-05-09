
input('''                                                                                                                        
                                  #      .     #                                                                        
                                  ##    ##    ##                                                                        
                                   #   ####   #   ####-#  # ##  # ##  ####x  X+.###                                     
                                   ##  #  #  -#  #     #  ##   X#    #=   ## ##    #                                    
                                    # #,  -# #  #,     #  #    X#   ## xx==# #-    #                                    
                                    ###    ###  ##     #  #    X#   ,#       #x    #                                    
                                     #      #    ###x###  #    x#    ,##xX#; #+    #                                    
                                                                                                                        
                                                                                                                        
                                      ###                            ##                                                 
                                     ####.                           ##                                                 
                                    ### ##    ######  #######  x#######  ######  ############ ###   ##,                 
                                    ##  ###  ###     ##    ##  ##    ## ###  ### ###  ###  ##x ##  ###                  
                                   ######### ##,     ##    ## ###    ## ###-+==x ##   ##x  ###  ## ##                   
                                  ### ,, =##  ###### ########  ########  ### ;#; ##   ###  ###  ####                    
                                  ##       #+  +###,   ### ;#   ,##X ##   -####  ##   +#   =#    ###                    
                                                         #################################################x             

Aperte ENTER para proceguir...''')
tempoChegada = 0
listafim = []

msg = input('''
    Um professor de programação, frustrado com a 
    falta de disciplina de seus alunos, decidi cancelar a 
    aula se menos de x alunos estiverem presentes quando a aula for 
    iniciada. O tempo de chegada varia entre:

    Normal: tempoChegada <= 0
    Atraso: tempoChegada > 0
            
Tecle ENTER para proceguir... ''')
#enquanto nao digita "sim" continua a executar o código 
while tempoChegada != "sim":
    tempoChegada = input('''
Digite os valores caso queira sair é só digitar "sim"
''')
    listafim.append(tempoChegada)
listafim2 = (listafim)[0:-1:]

#transforma tudo em inteiro
for i in range(len(listafim2)):
    listafim2[i] = int(listafim2[i])

listafim3 = []

#retorna todos o valores iguais ou abaixo de zero
for i in range(len(listafim2)):
    if listafim2[i] <=0:
        listafim3.append(listafim2[i])

 #recebe a quantidade de numeros igual ou abaixo de zero
listax = input('''
Qual o valor limite de alunos presentes? 
''')
listax = int(listax)

if listax <= (len(listafim3)) :
    print("AULA NORMAL")
    input("")
else:
    print("AULA CANCELADA")
    input("")



