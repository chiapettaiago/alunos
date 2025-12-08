#Bibliotecas necessárias importadas
from inserir_aluno import Aluno
from pesquisa_aluno import buscar_aluno, editar_aluno, remover_aluno

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
            inserir_aluno = Aluno("dados.csv")
            inserir_aluno.solicitarDados()
            inserir_aluno.salvar()
        elif escolha == "2":
            print("\n1. Pesquisar por Nome")
            print("2. Pesquisar por Matrícula")
            tipo_busca = input("Escolha o tipo de busca (1-2): ")
            
            id_encontrado = None
            
            if tipo_busca == "1":
                nome = input("Digite o nome que deseja buscar: ")
                id_encontrado = buscar_aluno("dados.csv", nome, tipo="nome")
            elif tipo_busca == "2":
                id_aluno = input("Digite a Matrícula que deseja buscar: ")
                id_encontrado = buscar_aluno("dados.csv", id_aluno, tipo="id")
            else:
                print("Opção inválida!")
                continue
            
            if id_encontrado is not None:
                print("\n1. Editar aluno")
                print("2. Remover aluno")
                print("3. Voltar")
                acao = input("Escolha uma ação (1-3): ").strip()
                
                if acao == "1":
                    editar_aluno("dados.csv", id_encontrado)
                elif acao == "2":
                    remover_aluno("dados.csv", id_encontrado)
                elif acao == "3":
                    continue
                else:
                    print("Opção inválida!")
        elif escolha == "3":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.\n")
            
#Inicia o loop principal do app
if __name__ == "__main__":
    loop()