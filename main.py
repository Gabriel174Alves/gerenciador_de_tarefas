import database
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

def exibir_menu():
    print(Back.MAGENTA + Fore.WHITE + Style.BRIGHT + "===========================")
    print(Fore.WHITE + Style.BRIGHT + "    GERENCIADOR DE TAREFAS   ")
    print(Back.MAGENTA + Fore.WHITE + "===========================")
    print(Fore.YELLOW + "1." + Fore.GREEN + " Adicionar Tarefa")
    print(Fore.YELLOW + "2." + Fore.GREEN + " Visualizar Tarefas")
    print(Fore.YELLOW + "3." + Fore.GREEN + " Marcar Tarefa Concluída")
    print(Fore.RED    + "4." + Fore.WHITE + " Remover Tarefa")
    print(Fore.RED    + "5." + Fore.WHITE + " Sair")
    print()

def main():
    while True:
        exibir_menu()
        opcao = input(Fore.CYAN + "Escolha uma opção: ").strip()

        if opcao == "1":
            desc = input(Fore.GREEN + "Descrição da tarefa: ")
            database.adicionar_tarefa(desc)
            print(Fore.GREEN + "✅ Tarefa adicionada!")
        elif opcao == "2":
            database.visualizar_tarefas()
        elif opcao == "3":
            try:
                tid = int(input(Fore.GREEN + "ID da tarefa para concluir: "))
                database.marcar_como_concluida(tid)
                print(Fore.GREEN + "🎉 Tarefa concluída!")
            except ValueError:
                print(Fore.RED + "ID inválido.")
        elif opcao == "4":
            try:
                tid = int(input(Fore.GREEN + "ID da tarefa para remover: "))
                database.remover_tarefa(tid)
                print(Fore.RED + "🗑️ Tarefa removida!")
            except ValueError:
                print(Fore.RED + "ID inválido.")
        elif opcao == "5":
            print(Fore.MAGENTA + "Até logo! 👋")
            break
        else:
            print(Fore.RED + "Opção inválida. Tente novamente.")
        print()  # linha em branco antes de reexibir o menu

if __name__ == "__main__":
    main()
