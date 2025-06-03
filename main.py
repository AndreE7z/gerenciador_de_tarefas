tarefas = []
proximo_id = 1

def adicionar_tarefa():
    global proximo_id
    descricao = input("\nDescrição da tarefa: ")
    tarefa = {
        "id": proximo_id,
        "descricao": descricao,
        "status": "Pendente"
    }
    tarefas.append(tarefa)
    print ("ID:", proximo_id)
    proximo_id += 1
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return
    print("\nLista de Tarefas:")
    for tarefa in tarefas:
        print(f"ID: {tarefa['id']} Descrição: {tarefa['descricao']} Status: {tarefa['status']}")

def marcar_concluida():
    try:
        id_tarefa = int(input("\nDigite o ID da tarefa a ser marcada como concluída: "))
        for tarefa in tarefas:
            if tarefa["id"] == id_tarefa:
                if tarefa["status"] == "Concluída":
                    print("Tarefa já está concluída.")
                else:
                    tarefa["status"] = "Concluída"
                    print("Tarefa marcada como concluída.")
                return
        print("Tarefa não encontrada.")
    except ValueError:
        print("ID inválido. Digite um número inteiro.")

while True:
    print("""
 Menu de Gerenciamento de Tarefas:
1. Adicionar nova tarefa
2. Listar todas as tarefas
3. Marcar tarefa como concluída
0. Sair""")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        marcar_concluida()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")