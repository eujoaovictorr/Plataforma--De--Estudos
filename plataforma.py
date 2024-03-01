conjuntos = []


# Função de menu onde o usuário escolherá a opção.
def menu():
    print('-' * 25)
    print('[1] Criar Conjunto')
    print('[2] Adicionar Elemento')
    print('[3] Remover Elemento')
    print('[4] Mostrar União entre elementos')
    print('[5] Encontrar a interseção entre conjuntos distintos')
    print('[6] Mostrar Conjuntos')
    print('[0] Sair')
    print('-' * 25)
    opcao = input("Escolha sua opção: ")
    return opcao


# Função de criar os conjuntos.
def criar_conjunto():
    conjuntos.append([])
    id = len(conjuntos)
    print(f"Conjunto {id} criado com êxito.")
    return id


# Função para adicionar os elementos ao conjunto.
def add_elementos(id, elemento):
    if id > len(conjuntos):
        print("Conjunto não encontrado")
    else:
        if elemento not in conjuntos[id-1]:
            conjuntos[id-1].append(elemento)
            print(f"Elemento {elemento} adicionado ao conjunto {id} com êxito.")
        else:
            print(f"Elemento {elemento} já pertence ao conjunto {id}.")


# Função para deletar os elementos do conjunto.
def del_elementos(id, elemento):
    if id > len(conjuntos):
        print("Conjunto não encontrado")
    else:
        if elemento in conjuntos[id-1]:
            conjuntos[id-1].remove(elemento)
            print(f"Elemento {elemento} removido do conjunto {id} com êxito.")
        else:
            print(f"Elemento {elemento} não pertence ao conjunto {id}.")


# Função para mostrar o conjunto.
def mostrar_conjuntos(id):
    if id > len(conjuntos):
        print("Conjunto não encontrado")
    else:
        print(f"Conjunto {id}: {conjuntos[id-1]}")

#def uniao(ids):

#def intersecao(ids):


while True:
    opcao = menu()
    if opcao == '1':
        criar_conjunto()
    elif opcao == '2':
        id = int(input("Digite o ID do conjunto: "))
        elemento = input("Digite o elemento a ser adicionado: ")
        add_elementos(id, elemento)
    elif opcao == '3':
        id = int(input("Digite o ID do conjunto: "))
        elemento = input("Digite o elemento a ser removido: ")
        del_elementos(id, elemento)
    elif opcao == '4':
        id = int(input("Digite o ID do conjunto: "))
        mostrar_conjuntos(id)
    elif opcao == '5':
        id = int(input("Digite o ID do conjunto: "))
        #intersecao(ids)
    elif opcao == '6':
        id = int(input("Digite o ID do conjunto: "))
        mostrar_conjuntos(id)
    elif opcao == '0':
        print("Saindo da plataforma.")
        break
    else:
        print("Opção errada.")


