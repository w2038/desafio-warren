
def processaCombinacao():
    global listaSubtraidos
    global numeroASerSubtraido
    global listaFinal
    global listaDeControle
    global tamMinListComRestoZero

    for i in listaSubtraidos:

        resto = numeroASerSubtraido
        # se o numero (subtraendo) for menor que o numero a ser subtraido ele pula para o proximo numero da lista
        if (i > numeroASerSubtraido):
            continue
        listaEmProcessamento = []

        idx = 0
        subtraendo = listaSubtraidos[idx]

        # se a lista de controle esta preenchida ele utiliza o ultimo numero da lista de subtraidos como 
        # subtraendo, e subtraio  o restante dos numeros da lista dos subtaidos do resto
        if (len(listaDeControle) > 0):
            listaEmProcessamento = listaDeControle
            ultimoNumeroDaLista = listaDeControle[len(listaDeControle)-1]
            idx = listaSubtraidos.index(ultimoNumeroDaLista)
            subtraendo = listaSubtraidos[idx]
            for valor in listaEmProcessamento:
                resto = resto - valor

        #enquanto o resto for positivo
        while resto > 0:
            # este valor é resevado quando ainda há numeros a serem usados na lista a aserem 
            # subtraidos e o resto apresentar valor negativo apos duas linhas abaixo
            restoOriginal = resto
            resto = resto - subtraendo
            
            if (resto > 0):
                listaEmProcessamento.append(subtraendo)
            elif (resto == 0):
                listaEmProcessamento.append(subtraendo)
                
                #lista criada para evitar associação ao ponteiro da lista em processamento
                listaTemporaria = []
                for valor in listaEmProcessamento:
                    listaTemporaria.append(valor)
                
                #verifica se a lista em processameto nao é maior que qualquer lista adicionada a lista total
                if (len(listaTemporaria) <= tamMinListComRestoZero):
                    listaFinal.append(listaTemporaria)
                    tamMinListComRestoZero = len(listaTemporaria)

                listaDeControle = listaEmProcessamento
                break; 

            else:
                # se o meu index  não estiver na ultima da lista de subtraidos 
                if (idx < len(listaSubtraidos) -1):
                    #avança o index, localiza o valor do subtraendo e retorna o valor do resto original
                    idx += 1
                    subtraendo = listaSubtraidos[idx]
                    resto = restoOriginal
                

                elif len(listaDeControle) == 0:
                    listaEmProcessamento.append(subtraendo)
                    listaDeControle = listaEmProcessamento
                else:
                    listaDeControle = listaEmProcessamento
        break

    #se a lista de controle não estiver vazia localiza o ultimo valor da lista de controle
    if (len(listaDeControle) > 0):
        ultimoNumeroDaLista = listaDeControle[len(listaDeControle)-1]
        #enquanto o ultimo numero da lista de controle for o menor valor da lista de suntraidos remove o 
        # ultimo valor da lista de controle
        while (ultimoNumeroDaLista == listaSubtraidos[len(listaSubtraidos)-1]):
            listaDeControle.pop(len(listaDeControle) -1)
            # se não houver mais valores a serem processados na lista de controle, encerra o processaCombinaçao()
            if (len(listaDeControle) == 0):
                return  
            # localiza o ultimo número da lista de controle 
            else:
                ultimoNumeroDaLista = listaDeControle[len(listaDeControle)-1]

        # localiza o ultimo numero da lista de controle, localiza a sua posição na lista de subtraidos e 
        # substitue o ultimo numero da lista de controle pelo proximo numero da lista de subtraidos
        ultimoNumeroDaLista == listaSubtraidos[len(listaSubtraidos)-1] 
        indexNaLista = listaSubtraidos.index(ultimoNumeroDaLista)
        listaDeControle[len(listaDeControle) -1] = listaSubtraidos[indexNaLista +1]
listaSubtraidos = []
valor = input("digite o valor a ser inserido na lista :")
while valor != 0 :
    listaSubtraidos.append(valor)
numeroASerSubtraido = 17
listaFinal = []
listaDeControle = []
tamMinListComRestoZero = 99999999

#oredena os numeros em forma decrescente
listaSubtraidos.sort(reverse=True)

#a primeira vez o processo  processaCombinacao a ser executado com a finalidade de obter
#  a lista com menor tamanho e com os maiores valores iniciais e só para de processar 
# quando lista de controle estiver vazia (final das combinações)
while True:
    processaCombinacao()
    if len(listaDeControle) == 0:
        break

input(listaFinal)
