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

import re


def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Thaynara Soares RA 25002736 & Vitória Mattos RA 25002891    |')
    print('|                                                             |')
    print('| Versão 2.0 de 19/maio/2025                                  |')
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


def cadastrar (agd):
    print("\n——— Cadastro de novo contato ———")
    print("\nOBS: caso deseje cancelar o cadastro digite 'cancela' no campo nome ")

    while True:
        padrao_de_nome = re.compile('^[A-Z][a-z]*(?: (?:[A-Z]|[a-z])[a-z]*)*$')
        nome = input("Nome.......: ")

        if not padrao_de_nome.match(nome):
            print("Nome inválido, tente novamente!")
            continue
        achou, posicao = ondeEsta(nome, agd)

        if nome.lower() == "cancela":
            print("Cadastro cancelado.")
            return

        if achou:
            print("Este nome já está cadastrado. Por favor, insira um nome diferente.")
        else:
            break 

    while True:
        padrao_aniversario = re.compile ('^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[0-2])/\d{4}$')
        aniversario = input("Aniversário: ")
        if padrao_aniversario.match(aniversario):
            break
        else:
            print("Aniversário inválido, digite no formato (DD/MM/AAAA). Tente novamente!")

    while True:        
        padrao_endereco = re.compile('^[A-Za-zÀ-ÿ0-9 ,.\-ºª]+$')
        endereco = input("Endereço.... ")
        if padrao_endereco.match(endereco):
            break
        else:
            print("Endereço inválido, tente novamente!")
    while True:
        padrao_de_telefone = re.compile('^\(\d{2}\) \d{4}-\d{4}$')
        telefone = input("Telefone.... ")
        if padrao_de_telefone.match(telefone):
            break
        else:
            print("Telefone inválido, digite no formato (XX) XXXX-XXXX. Tente novamente!")

    while True:
        padrao_de_celular = re.compile('^\(\d{2}\) 9\d{4}-\d{4}$')
        celular = input("Celular..... ")
        if padrao_de_celular.match(celular):
            break
        else:
            print("Celular inválido, digite no formato (XX) XXXXX-XXXX. Tente novamente!")

    while True:
        padrao_email = re.compile('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        email = input("E-mail...... ")
        if padrao_email.match(email):
            break
        else:
            print("Email inválido, tente novamente!")

    contato = [nome, aniversario, endereco, telefone, celular, email]

    agd.insert(posicao, contato)
    print("Contato cadastrado com sucesso!")
        

def procurar (agd):
    print("\n——— Procurar contato ———")
    while True:
        nome = input("Digite o nome do contato que deseja procurar (ou 'cancela' para desistir): ")

        if nome.lower() == "cancela":
            print("Busca cancelada.")
            return

        achou, posicao = ondeEsta(nome, agd)
        if not achou:
            print("Nome não encontrado. Tente novamente!")
        else:
            if achou:
                contato = agd[posicao]
                print("\nContato encontrado:")
                print("Nome.......:", contato[0])
                print("Aniversário:", contato[1])
                print("Endereço...:", contato[2])
                print("Telefone...:", contato[3])
                print("Celular....:", contato[4])
                print("E-mail.....:", contato[5])
                break


def atualizar (agd):
    print("\n——— Atualizar contato ———")

    while True:
        nome = input("Digite o nome do contato que deseja alterar(ou 'cancela' para desistir): ")

        if nome.lower() == "cancela":
            print("Busca cancelada.")
            return
    
        achou, posicao = ondeEsta(nome, agd)
        
        if not achou:
            print("Nome não cadastrado. Tente novamente!")
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
                    while True:
                        padrao_aniversario = re.compile ('^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[0-2])/\d{4}$')
                        novo_aniversario = input("Digite a nova data de aniversário (ou 'cancela' para desistir): ")
                
                        if novo_aniversario.lower() == "cancela":
                            print("Atualização do aniversário cancelada.")
                            break

                        elif padrao_aniversario.match(novo_aniversario):
                            agd[posicao][1]= novo_aniversario
                            print("Aniversário atualizado com sucesso!")
                            break
                        else:
                            print("Aniversário inválido, digite no formato (DD/MM/AAAA). Tente novamente!")


                elif opcao == 2:
                    while True:
                        padrao_endereco = re.compile('^[A-Za-zÀ-ÿ0-9 ,.\-ºª]+$')
                        novo_endereco = input("Digite o novo endereço (ou 'cancela' para desistir): ")

                        if novo_endereco.lower() == "cancela":
                            print("Atualização do endereço cancelada.")
                            break
                        
                        elif padrao_endereco.match(novo_endereco):
                            agd[posicao][2]= novo_endereco
                            print("Endereço atualizado com sucesso!")
                            break     
                        else:
                            print("Endereço inválido, tente novamente!")

                elif opcao == 3:
                    while True:
                        padrao_de_telefone = re.compile('^\(\d{2}\) \d{4}-\d{4}$')
                        novo_telefone = input("Digite o novo telefone (ou 'cancela' para desistir): ")

                        if novo_telefone.lower() == "cancela":
                            print("Atualização do telefone cancelada.")
                            break
                        
                        elif padrao_de_telefone.match(novo_telefone):  
                            agd[posicao][3] = novo_telefone
                            print("Telefone atualizado com sucesso!")
                            break
                        else:
                            print("Telefone inválido, digite no formato (XX) XXXX-XXXX. Tente novamente!")
        

                elif opcao == 4:
                    while True:
                        padrao_de_celular = re.compile('^\(\d{2}\) 9\d{4}-\d{4}$')
                        novo_celular = input("Digite o novo celular (ou 'cancela' para desistir): ")

                        if novo_celular.lower() == "cancela":
                            print("Atualização do celular cancelada.")
                            break

                        elif padrao_de_celular.match(novo_celular):
                            agd[posicao][4]= novo_celular
                            print("Celular atualizado com sucesso!")
                            break
                        else:
                            print("Celular inválido, digite no formato (XX) XXXXX-XXXX. Tente novamente!")


                elif opcao == 5:
                    while True:
                        padrao_email = re.compile('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
                        novo_email = input("Digite o novo email (ou 'cancela' para desistir): ")

                        if novo_email.lower() == "cancela":
                            print("Atualização do email cancelada.")
                            break

                        elif padrao_email.match(novo_email):
                            agd[posicao][5] = novo_email
                            print("Email atualizado com sucesso!")
                            break
                        else:
                            print("Email inválido, tente novamente!")
                        

                elif opcao == 6:
                    deseja_terminar_atualizacao = True
                    print("Atualização finalizada.")
                else:
                    print("Opção inválida. Tente novamente.")

            return

        
def listar (agd):
    print("\n——— Lista de contatos ———")

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
    print("\n——— Excluir contato ———")

    while True:
        nome = input("Digite o nome do contato que deseja excluir (ou 'cancela' para desistir): ")

        if nome.lower() == "cancela":
            print("Busca cancelada.")
            return
    
        achou, posicao = ondeEsta(nome, agd)
        
        if not achou:
            print("Nome não cadastrado. Tente novamente!")
        else:
            contato = agd[posicao]
            print("\nContato encontrado:")
            print(f"Nome.......: {contato[0]}")
            print(f"Aniversário: {contato[1]}")
            print(f"Endereço...: {contato[2]}")
            print(f"Telefone...: {contato[3]}")
            print(f"Celular....: {contato[4]}")
            print(f"E-mail.....: {contato[5]}")

            confirma = input("Deseja realmente excluir este contato? (s/n): ").lower()

            if confirma == "s":
                del agd[posicao]
                print("Contato excluído com sucesso!")
            else:
                print("Exclusão cancelada!")
            return
    
    
    
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
    else: 
        deseja_terminar_o_programa=True
        
print('PROGRAMA ENCERRADO COM SUCESSO!')


