import json

def carregar_dados():
    try:
        with open('dados.json', 'r') as arquivo_json:
            dados = json.load(arquivo_json)
    except FileNotFoundError:
        dados = {
            "alunos": {},
            "turmas": {},
            "ciclos": {},
            "grupos": {},
            "notas": {}
        }
    return dados

def editar_grupo():
    dados = carregar_dados()
    grupo_id = input("Informe o ID do grupo a ser editado: ")
    if grupo_id in dados['grupos']:
        grupo = dados['grupos'][grupo_id]
        print(f'Editando dados do grupo ID: {grupo_id}')
        while True:
            print(f'1 - Nome: {grupo["nome"]}')
            print('Alunos no grupo:')
            for ra_aluno in grupo['alunos']:
                if ra_aluno in dados['alunos']:
                    aluno = dados['alunos'][ra_aluno]
                    print(f' - RA: {aluno["ra"]}, Nome: {aluno["nome"]}')
                else:
                    print(f' - RA: {ra_aluno}, Aluno não encontrado no sistema')

            campo = input('Escolha o campo que deseja editar (1 para Nome, 2 para adicionar aluno, 3 para remover aluno, 4 para cancelar, 5 para salvar): ')
            if campo == '1':
                grupo['Nome'] = input('Novo Nome: ')
            elif campo == '2':
                ra_aluno = input('Informe o RA do aluno a ser adicionado: ')
                if ra_aluno in dados['alunos']:
                    grupo['Alunos'].append(ra_aluno)
                    print(f'Aluno com RA {ra_aluno} adicionado ao grupo.')
                else:
                    print(f"O aluno com RA {ra_aluno} não existe no sistema.")
            elif campo == '3':
                ra_aluno = input('Informe o RA do aluno a ser removido: ')
                if ra_aluno in grupo['Alunos']:
                    grupo['Alunos'].remove(ra_aluno)
                    print(f'Aluno com RA {ra_aluno} removido do grupo.')
                else:
                    print(f"O aluno com RA {ra_aluno} não está no grupo.")
            elif campo == '4':
                break
            elif campo == '5':
                dados['grupos'][grupo_id] = grupo
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
        print(f'O grupo com ID {grupo_id} não foi encontrado.')
        return False
