import json

def carregar_dados_alunos():
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

def editar_turma():
    dados = carregar_dados_alunos()
    turma_id = input("\nQual o ID da turma que você quer editar?\n")
    if turma_id in dados['turmas']:
        turma = dados['turmas'][turma_id]
        print(f'Editando dados da turma ID: {turma_id}')
        while True:
            print(f'1 - Nome: {turma["nome"]}')

            campo = input('Escolha o campo que deseja editar (1), 2 para cancelar ou 3 para salvar: ')
            if campo == '1':
                turma['nome'] = input('Novo Nome: ')
            elif campo == '2':
                break
            elif campo == '3':
                dados['turmas'][turma_id] = turma
                with open('dados.json', 'w') as arquivo_json:
                    json.dump(dados, arquivo_json, indent=4)
                print('Cadastro atualizado com sucesso.')
                return True
            else:
                print('Opção inválida. Tente novamente.')
        if campo != '2':
            print('Cadastro atualizado com sucesso.')
            return False
    else:
        print(f'A turma com ID {turma_id} não foi encontrada.')
        return False
