## Gerenciamento de alunos

Programa de genrenciamento de alunos escrito em Python para a disciplina de Princípios de Construção de Algoritmos.

Criado pelo aluno:

- Nome: Iago Filgueiras Chiapetta
- Matrícula: 06009919

## Instalação

 - Clone o repositório git usando o comando:
```
git clone https://github.com/chiapettaiago/alunos.git
```
- Após isso, entre na pasta trabalho_pca com o comando:
```
cd trabalho_pca
```

 - Agore instale os pacotes necessários:
 ```
 pip install -r requirements.txt
 ```

 - Por último rode o sistema
 
 No Windows:
 ```
 python app.py
 ```

 No Linux:
 ```
 python3 app.py
 ```

## Comandos disponíveis (menu)

- `1 - Inserir`: cadastra um novo aluno (gera ID automático) pedindo Nome, Rua, Bairro, Cidade, UF, Telefone e Email.
- `2 - Pesquisar`: permite buscar por `Nome` (parcial, sem diferenciar maiúsculas/minúsculas) ou por `Matrícula/ID` (valor exato). Após encontrar um aluno, o sistema oferece:
	- `1 - Editar aluno`: altera os campos informados (deixe em branco para manter o valor atual).
	- `2 - Remover aluno`: exclui o registro após confirmação.
	- `3 - Voltar`: retorna ao menu principal.
- `3 - Sair`: encerra o programa.

 
