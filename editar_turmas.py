import json
from listagem import listar_turmas
from listagem import listar_alunos

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

def listar_alunos_turma(dados, turma):
    if 'alunos' in turma and isinstance(turma['alunos'], list):
        print("\nLista de Alunos na Turma:")
        for ra in turma['alunos']:
            if ra in dados['alunos']:
                aluno = dados['alunos'][ra]
                print(f"RA: {ra}, Nome: {aluno['nome']}")
        print("\n")
    else:
        print("Nenhum aluno cadastrado nesta turma.\n")

def editar_turma():
    dados = carregar_dados_alunos()
    listar_turmas(dados)
    turma_id = input("\nQual o ID da turma que você quer editar?\n")

    if turma_id in dados['turmas']:
        turma = dados['turmas'][turma_id]
        print(f'Editando dados da turma ID: {turma_id}')

        while True:
            print(f'1 - Nome: {turma["nome"]}')

            campo = input('Escolha o campo que deseja editar:  \n1 nome\n2 para inserir aluno\n3 para remover aluno\n4 para cancelar\n5 para salvar \n')

            if campo == '1':
                turma['nome'] = input('Novo Nome: ')

            elif campo == '2':
                listar_alunos(dados)
                aluno_ra = input('Informe o RA do aluno que deseja adicionar à turma: ')
                if aluno_ra in dados['alunos']:
                    if 'turmas' not in dados['alunos'][aluno_ra]:
                        dados['alunos'][aluno_ra]['turmas'] = []
                    if turma_id not in dados['alunos'][aluno_ra]['turmas']:
                        dados['alunos'][aluno_ra]['turmas'].append(turma_id)
                        if 'alunos' not in turma:
                            turma['alunos'] = []
                        turma['alunos'].append(aluno_ra)
                        print(f'Aluno adicionado à turma {turma_id} com sucesso.')
                    else:
                        print('Este aluno já está na turma.')
                else:
                    print('Aluno não encontrado.')

            elif campo == '3':
                listar_alunos_turma(dados, turma)
                aluno_ra = input('Informe o RA do aluno que deseja remover da turma: ')
                if 'alunos' in turma and aluno_ra in turma['alunos']:
                    turma['alunos'].remove(aluno_ra)
                    dados['alunos'][aluno_ra]['turmas'].remove(turma_id)
                    print(f'Aluno removido da turma {turma_id} com sucesso.')
                else:
                    print('Este aluno não está na turma.')

            elif campo == '4':
                break

            elif campo == '5':
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
