
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

lista = []
listaImpares = []
valorEntrada = 10000

#pega numero impares acima de 10 e colorca na lista de impares 
for indice in range(valorEntrada):
    if (indice %2 == 1):
        listaImpares.append(indice)

for indice in listaImpares:
    #valor recebe os valors em string e verifica se se a soma 
    # do primeiro numro com o ultimo já tranformados em numero
    valor = list(str(indice))
    primeiroNumero = ((int(valor[0]) +2))
    ultimoNumero = ((int(valor[len(valor)-1])) +2)

    #se a soma do primeiro com o ultimo for impar armazena na lista 
    if ((primeiroNumero %2) + (ultimoNumero %2) == 1):
        lista.append(indice)

# for i in lista:
#     (print(i))
print(f' lista de números que podem ser somados com seu reverso que resulta em numero ímpar: ', lista )
print("resulta ", len(lista), " númenoros abaixo de 1000000")
input("")