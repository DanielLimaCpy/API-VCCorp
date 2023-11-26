import json



def carregar_dados():
    try:
        with open('dados.json', 'r') as arquivo_dados_alunos_json:
            dados_alunos = json.load(arquivo_dados_alunos_json)
    except FileNotFoundError:
        # Se o arquivo não existir, cria uma estrutura vazia
        dados_alunos = {
            "alunos": {},
            "turmas": {},
            "ciclos": {},
            "grupos": {},
            "notas": {}
        }
    return dados_alunos

def editar_aluno(ra_aluno):
    dados = carregar_dados()
    if ra_aluno in dados['alunos']:
        aluno = dados['alunos'][ra_aluno]
        print(f'Editando dados do aluno RA: {ra_aluno}')
        while True:
            print(f'1 - Nome: {aluno["nome"]}')
            print(f'2 - Idade: {aluno["idade"]}')
            print(f'3 - E-mail: {aluno["email"]}')

            campo = input('Escolha o campo que deseja editar (1/2/3), 4 para cancelar ou 5 para salvar: ')
            if campo == '1':
                aluno['nome'] = input('Novo Nome: ')
            elif campo == '2':
                aluno['idade'] = input('Nova Idade: ')
            elif campo == '3':
                aluno['email'] = input('Novo E-mail: ')
            elif campo == '4':
                break
            elif campo == '5':
                dados['alunos'][ra_aluno] = aluno
                with open('dados.json', 'w') as arquivo_json:
                    json.dump(dados, arquivo_json, indent=4)
                print('Cadastro atualizado com sucesso.')
                return True
            else:
                print('Opção inválida. Tente novamente.')
        if campo != '4':
            print('Cadastro atualizado com sucesso.')
            return False
    else:
        print(f'O aluno com RA {ra_aluno} não foi encontrado.')
        return False
