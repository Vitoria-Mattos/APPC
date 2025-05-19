'''
Implementar a opções do menu, sempre cuidando de validar os inputs do
usuário.
Usar, sempre que cabível, as funções prontas no código.

Fazer o trabalho em duplas e entregar duas semanas, ou seja, NÃO na
próxima aula, na seguinte.
Substituir, na função apresenteSe, o texto:
"Profs André Carvalho & J.G.Pícolo"
por um texto contendo os nomes e RAs dos alunos da dupla.
Também substituir o texto:
"Versão 1.0 de 12/maio/2025"
por
"Versão 2.0 de dd/mm/aaaa"
sendo dd/mm/aaaa a data que que a dupla concluiu seu trabalho.

A entrega será na forma de demonstração ao professor; os dois da dupla
deverão estar presentes na entrega e serão questionados pelo professor
sobre o programa que apresentam.
IMPORTANTE: este questionamento poderá resultar em notas diferentes para
os alunos da dupla, ou até em uma nota bem baixa para um programa que
funciona perfeitamente (basta estar perdido na demonstração).
'''




def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Thaynara Soares RA 25002736 & Vitória Mattos RA 25002891    |')
    print('|                                                             |')
    print('| Versão 2.0 de 26/maio/2025                                  |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')

def umTexto (solicitacao, mensagem, valido):
    digitouDireito=False
    while not digitouDireito:
        txt=input(solicitacao)

        if txt not in valido:
            print(mensagem,'- Favor redigitar...')
        else:
            digitouDireito=True

    return txt

def opcaoEscolhida (mnu):
    print()

    opcoesValidas=[]
    posicao=0
    while posicao<len(mnu):
        print (posicao+1,') ',mnu[posicao],sep='')
        opcoesValidas.append(str(posicao+1))
        posicao+=1

    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)

'''
procura nom em agd e, se achou, retorna:
uma lista contendo True e a posicao onde achou;
MAS, se não achou, retorna:
uma lista contendo False e a posição onde inserir,
aquilo que foi buscado, mas nao foi encontrado,
mantendo a ordenação da lista.
'''
def ondeEsta (nom,agd):
    inicio=0
    final =len(agd)-1
    
    while inicio <= final:
        meio=(inicio+final)//2
        if agd[meio][0] == nom:
            return [True, meio]
        elif agd[meio][0] > nom:
            final = meio - 1 
        else:
            inicio = meio + 1
    
    return[False, inicio]


    # continue a implementação que, entre outras coisas, deverá
    # calcular o meio, conforme segue:
        
    # a função deverá retornar a lista [True,meio] quando encontrar o
    # nome procurado ou então a lista [False,inicio], quando não
    # encontrar o nome procurado.

def cadastrar (agd):
    print("\n>>> Cadastro de novo contato <<<")

    nome = input("Nome.......: ")
    achou, posicao = ondeEsta(nome, agd)

    if achou:
        print("Este nome já está cadastrado.")
        return
    else:
        aniversario = input("Aniversário: ")
        endereco = input("Endereço.... ")
        telefone = input("Telefone.... ")
        celular = input("Celular..... ")
        email = input("E-mail...... ")

        contato = [nome, aniversario, endereco, telefone, celular, email]

        agd.insert(posicao, contato)
        print("Contato cadastrado com sucesso!")
    

def procurar (agd):
    print("\n>>> Procurar contato <<<")
    nome = input("Digite o nome do contato que deseja procurar (ou 'cancela' para desistir): ")

    if nome.lower() == "cancela":
        print("Busca cancelada.")
        return

    achou, posicao = ondeEsta(nome, agd)

    if achou:
        contato = agd[posicao]
        print("\nContato encontrado:")
        print("Nome.......:", contato[0])
        print("Aniversário:", contato[1])
        print("Endereço...:", contato[2])
        print("Telefone...:", contato[3])
        print("Celular....:", contato[4])
        print("E-mail.....:", contato[5])
    else:
        print("Contato não encontrado.")


def atualizar (agd):
    print("\n>>> Atualizar contato <<<")

    while True:
        nome = input("Digite o nome do contato que deseja alterar(ou 'cancela' para desistir): ")

        if nome.lower() == "cancela":
            print("Busca cancelada.")
            return
    
        achou, posicao = ondeEsta(nome, agd)
        
        if not achou:
            print("Nome não cadastrado!")
        else:
            submenu=['Atualizar aniversário',\
                    'Atualizar endereço',\
                    'Atualizar telefone',\
                    'Atualizar celular',\
                    'Atualizar email',\
                    'Finalizar alterações']
        
            deseja_terminar_atualizacao=False
            while not deseja_terminar_atualizacao:
                opcao = int(opcaoEscolhida(submenu))

                if opcao == 1:
                    novo_aniversario = input("Digite a nova data de aniversário (ou 'cancela' para desistir): ")
                    if novo_aniversario.lower() == "cancela":
                        print("Atualização do aniversário cancelada.")
                    else:
                        agd[posicao][1]= novo_aniversario
                        print("Aniversário atualizado com sucesso!")

                elif opcao == 2:
                    novo_endereco = input("Digite o novo endereço (ou 'cancela' para desistir): ")
                    if novo_endereco.lower() == "cancela":
                        print("Atualização do endereço cancelada.")
                    else:
                        agd[posicao][2]= novo_endereco
                        print("Endereço atualizado com sucesso!")

                elif opcao == 3:
                    novo_telefone = input("Digite o novo telefone (ou 'cancela' para desistir): ")
                    if novo_telefone.lower() == "cancela":
                        print("Atualização do telefone cancelada.")
                    else:
                        agd[posicao][3] = novo_telefone
                        print("Telefone atualizado com sucesso!")

                elif opcao == 4:
                    novo_celular = input("Digite o novo celular (ou 'cancela' para desistir): ")
                    if novo_celular.lower() == "cancela":
                        print("Atualização do celular cancelada.")
                    else:
                        agd[posicao][4]= novo_celular

                        print("Celular atualizado com sucesso!")

                elif opcao == 5:
                    novo_email = input("Digite o novo email (ou 'cancela' para desistir): ")
                    if novo_email.lower() == "cancela":
                        print("Atualização do email cancelada.")
                    else:
                        agd[posicao][5] = novo_email
                        print("Email atualizado com sucesso!")

                elif opcao == 6:
                    deseja_terminar_atualizacao = True
                    print("Atualização finalizada.")

                else:
                    print("Opção inválida. Tente novamente.")

            return

        
    # Ficar solicitando a digitação de um nome a ser excluido da agenda,
    # até que um nome cadastrado seja digitado.
    # Ficar mostrando então um SUBMENU oferecendo as opções de atualizar
    # aniversário, ou endereco, ou telefone, ou celular, ou email, ou
    # finalizar as atualizações; ficar pedindo para digitar a opção até
    # digitar uma opção válida; realizar a atulização solicitada; tudo
    # isso até ser escolhida a opção de finalizar as atualizações.
    # REPARE que não foi prevista uma opção de atualizar o nome!
    # USAR A FUNÇÃO opcaoEscolhida, JÁ IMPLEMENTADA, PARA FAZER O MENU.
    # O usuário poderá desistir de atualizar, escrevendo "cancela" no
    # momento de digitar o nome a ser atualizado, ou, até mesmo, no
    # momento de digitar o aniversário ou o endereço ou o telefone (fixo)
    # ou o celular ou ainda o e_mail (caso o usuário tenha optado por
    # uma dessas atualizações, naturalmente).

def listar (agd):
    print("\n>>> Lista de contatos <<<")

    if len(agd) == 0:
        print("Agenda vazia!")
        return
    
    for contato in agd:
        print(f"\nNome.......: {contato[0]}")
        print(f"Aniversario: {contato[1]}")
        print(f"Endereco...: {contato[2]}")
        print(f"Telefone...: {contato[3]}")
        print(f"Celular....: {contato[4]}")
        print(f"E-mail.....: {contato[5]}")


def excluir (agd):
    print("\n>>> Excluir contato <<<")

    while True:
        nome = input("Digite o nome do contato que deseja excluir (ou 'cancela' para desistir): ")

        if nome.lower() == "cancela":
            print("Busca cancelada.")
            return
    
        achou, posicao = ondeEsta(nome, agd)
        
        if not achou:
            print("Nome não cadastrado!")
        else:
            # Mostrar dados do contato
            contato = agd[posicao]
            print("\nContato encontrado:")
            print(f"Nome: {contato[0]}")
            print(f"Aniversário: {contato[1]}")
            print(f"Endereço: {contato[2]}")  #não está aparecendo arrumar
            print(f"Telefone: {contato[3]}")
            print(f"Celular: {contato[4]}")
            print(f"E-mail: {contato[5]}")

            # Solicitar confirmação
            confirma = input("Deseja realmente excluir este contato? (s/n): ").lower()

            if confirma == "s":
                del agd[posicao]
                print("Contato excluído com sucesso!")
            else:
                print("Exclusão cancelada!")
            return
    
    
    # Ficar solicitando a digitação de um nome a ser excluido da agenda,
    # até que um nome cadastrado seja digitado.
    # Os dados encontrados deveriam então ser mostrados e a exclusão!!!!!!!!!!!!!!!!!!!!!!
    # deveria ser confirmada.
    # Sendo confirmada, a exclusão deveria ser realizada e uma mensagem
    # de exclusão bem sucedida deveria ser mostrada. Não sendo confirmada,
    # uma mensagem de exclusão não realizada deveria ser mostrada.
    # O usuário poderá desistir de excluir, escrevendo "cancela" no
    # momento de digitar o nome a ser excluído.
    
    
    
# daqui para cima, definimos subprogramas (ou módulos, é a mesma coisa)
# daqui para baixo, implementamos o programa
# (nosso CRUD, C=create(cadastrar), R=read(recuperar),
# U=update(atualizar), D=delete(remover,apagar)




apresenteSe()

agenda=[] # essa é a listona que deverá conter listinhas

menu=['Cadastrar Contato',\
      'Procurar Contato',\
      'Atualizar Contato',\
      'Listar Contatos',\
      'Excluir Contato',\
      'Sair do Programa']

deseja_terminar_o_programa=False
while not deseja_terminar_o_programa:
    opcao = int(opcaoEscolhida(menu))

    if opcao==1:
        cadastrar(agenda)
    elif opcao==2:
        procurar(agenda)
    elif opcao==3:
        atualizar(agenda)
    elif opcao==4:
        listar(agenda)
    elif opcao==5:
        excluir(agenda)
    else: # opcao==6
        deseja_terminar_o_programa=True
        
print('PROGRAMA ENCERRADO COM SUCESSO!')


