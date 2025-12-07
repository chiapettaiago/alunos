import pandas as pd
import os

class Aluno:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        
    def solicitarDados(self):
        self.nome = input("Nome: ")
        self.rua = input("Rua: ")
        self.bairro = input("Bairro: ")
        self.cidade = input("Cidade: ")
        self.uf = input("UF: ")
        self.telefone = input("Telefone: ")
        self.email = input("Email: ")

    def __repr__(self):
        return f"Aluno(nome={self.nome}, rua={self.rua}, bairro={self.bairro}, cidade={self.cidade}, uf={self.uf}, telefone={self.telefone}, email={self.email})"
    
    def salvar(self):
        dados = {
            "Nome": [self.nome],
            "Rua": [self.rua],
            "Bairro": [self.bairro],
            "Cidade": [self.cidade],
            "UF": [self.uf],
            "Telefone": [self.telefone],
            "Email": [self.email]
        }
        df_novo = pd.DataFrame(dados)
        
        if os.path.exists(self.arquivo):
            df_existente = pd.read_csv(self.arquivo)
            proximo_id = df_existente['ID'].max() + 1
            df_novo['ID'] = proximo_id
            df_atualizado = pd.concat([df_existente, df_novo], ignore_index=True)
        else:
            df_novo['ID'] = 1
            df_atualizado = df_novo
        
        df_atualizado = df_atualizado[['ID', 'Nome', 'Rua', 'Bairro', 'Cidade', 'UF', 'Telefone', 'Email']]
        df_atualizado.to_csv(self.arquivo, index=False)
        print("Aluno inserido com sucesso!\n")