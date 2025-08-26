tarefas = []

def adicionar_tarefa(descricao, prazo=None, urgencia="Normal"):
    tarefa = {
        "id": len(tarefas) + 1,
        "descricao": descricao,
        "status": "Pendente",
        "prazo": prazo,
        "urgencia": urgencia
    }
    tarefas.append(tarefa)
    return tarefa

def listar_tarefas():
   # lista todas as tarefas armazenadas
    if not tarefas:
        print("nenhuma tarefa encontrada")
    else:
        for t in tarefas:
            print(f"[{t['id']}] {t['descricao']} - Status: {t['status']} | Prazo: {t['prazo']} | Urgência: {t['urgencia']}")

def marcar_concluida(id_tarefa):
    # marca uma tarefa específica como concluida pelo id
    for t in tarefas:
        if t["id"] == id_tarefa:
            t["status"] = "Concluída"
            print(f"tarefa '{t['descricao']}' concluída!")
            return
    print("tarefa não encontrada")

def remover_tarefa(id_tarefa):
    # remove uma tarefa tambem pelo id
    global tarefas
    for t in tarefas:
        if t["id"] == id_tarefa:
            tarefas.remove(t)
            print(f"tarefa '{t['descricao']}' removida com sucesso!")
            return
    print("tarefa não encontrada")

def menu():
    #exibe na tela o menu de opcoes
    while True:
        print("\n===== Gestão de Tarefas =====")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            #le os dados da tarefa 
            desc = input("Descrição da tarefa: ")
            prazo = input("Prazo: ") or None
            urg = input("Urgência (Baixa, Normal, Alta): ") or "Normal"
            adicionar_tarefa(desc, prazo, urg)

        elif opcao == "2":
            listar_tarefas()

        elif opcao == "3":
            try:
                id_t = int(input("Digite o ID da tarefa: "))
                marcar_concluida(id_t)
            except ValueError:
                print("digite um número válido")

        elif opcao == "4":
            try:
                id_t = int(input("Digite o ID da tarefa: "))
                remover_tarefa(id_t)
            except ValueError:
                print("Digite um número válido.")

        elif opcao == "5":
            print("Saindo do sistema...")
            #encerra o programa 
            break

        else:
            print("opção inválida! Tente novamente")

menu()
