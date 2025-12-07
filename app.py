
#Loop principal do app
def loop():
    while True:
        print("Gerenciamento de alunos \n")
        print("Escolha uma opção:\n ")
        print("1 - Inserir")
        print("2 - Pesquisar")
        print("3 - Sair \n")
        escolha = input("Opção:  ").strip().lower()
        if escolha == "1":
            inserir_aluno()
        elif escolha == "2":
            pesquisar_aluno()
        elif escolha == "3":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")
            
#Inicia o loop principal do app
if __name__ == "__main__":
    loop()