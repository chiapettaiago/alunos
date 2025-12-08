# folha.py
import pandas as pd
import os

def ler_folha(arquivo):
    if not os.path.isfile(arquivo):
        print("Nenhum dado encontrado!")
        return None
    
    df = pd.read_csv(arquivo, encoding="utf-8")
    
    # Garante a coluna ID e preenche NaN com sequência
    if "ID" not in df.columns:
        df.insert(0, "ID", range(1, len(df) + 1))
    else:
        # Se houver NaN ou não for inteiro, gera IDs sequenciais
        if df["ID"].isna().any():
            df["ID"] = pd.Series(range(1, len(df) + 1), dtype="Int64")
        else:
            df["ID"] = df["ID"].astype("Int64")
    
    # Salva de volta caso tenha sido corrigido
    df.to_csv(arquivo, index=False)
    return df

def buscar_aluno(arquivo, criterio, tipo="nome"):
    df = ler_folha(arquivo)
    if df is None:
        return None

    if tipo == "id":
        try:
            criterio = int(criterio)
            resultado = df[df["ID"] == criterio]
        except ValueError:
            print("ID inválido! Digite um número.")
            return None
    else:
        resultado = df[df["Nome"].str.contains(criterio, case=False, na=False)]

    if resultado.empty:
        print(f"Nenhum aluno encontrado com o {tipo} '{criterio}'.")
        return None
    
    print("\n=== RESULTADO DA PESQUISA ===\n")
    print(resultado.to_string(index=False))
    print("\n==============================\n")
    
    # Se múltiplos, pedir seleção
    if len(resultado) > 1:
        id_selecionado = input("Digite o ID do aluno que deseja selecionar: ").strip()
        try:
            return int(id_selecionado)
        except ValueError:
            print("ID inválido!")
            return None
    
    id_valor = resultado.iloc[0]["ID"]
    if pd.isna(id_valor):
        print("Registro sem ID válido.")
        return None
    return int(id_valor)
        
def editar_aluno(arquivo, id_aluno):
    df = ler_folha(arquivo)
    if df is None:
        return
    
    indice = df[df["ID"] == id_aluno].index[0]
    
    print("\nDigite os novos dados (deixe em branco para manter o valor atual):\n")
    
    campos = ["Nome", "Rua", "Bairro", "Cidade", "UF", "Telefone", "Email"]
    
    for campo in campos:
        novo_valor = input(f"{campo} [{df.loc[indice, campo]}]: ").strip()
        if novo_valor:
            df.loc[indice, campo] = novo_valor
    
    df.to_csv(arquivo, index=False)
    print("Aluno editado com sucesso!\n")

def remover_aluno(arquivo, id_aluno):
    df = ler_folha(arquivo)
    if df is None:
        return
    
    confirmacao = input(f"Tem certeza que deseja remover o aluno com ID {id_aluno}? (s/n): ").strip().lower()
    
    if confirmacao == "s":
        df = df[df["ID"] != id_aluno]
        df.to_csv(arquivo, index=False)
        print("Aluno removido com sucesso!\n")
    else:
        print("Operação cancelada.\n")
