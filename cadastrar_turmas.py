import json
from editar_turmas import editar_turma

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

def func_cadastrar_turmas():
    dados = carregar_dados()
    while True:
        id_turma = input('Informe o ID da turma a ser cadastrada: ')
        if id_turma in dados['turmas']:
            print('O ID já está cadastrado. O que deseja fazer?')
            opcao = input('1 - Criar uma nova turma\n2 - Editar os dados da turma\n')
            if opcao == '1':
                continue
            elif opcao == '2':
                editar_turma(id_turma, dados)
                return False
        else:
            nome_turma = input('Qual o nome da turma? ')
            data_inicio = input('Qual a data de início da turma? ')

            nova_turma = {
                'id': id_turma,
                'nome': nome_turma,
                'data_de_inicio': data_inicio,
                
            }

            dados['turmas'][id_turma] = nova_turma
            with open('dados.json', 'w') as arquivo_json:
                json.dump(dados, arquivo_json, indent=4)
            print('Cadastro da turma realizado com sucesso.')

            # Pergunta se deseja inserir alunos na turma
            inserir_alunos = input('Deseja inserir alunos nesta turma? (S/N): ')
            if inserir_alunos.lower() == 's':
                while True:
                    ra_aluno = input('Informe o RA do aluno a ser inserido na turma (ou "0" para encerrar): ')
                    if ra_aluno == '0':
                        break
                    if ra_aluno in dados['alunos']:
                        if 'turmas' not in dados['alunos'][ra_aluno]:
                            dados['alunos'][ra_aluno]['turmas'] = []
                        dados['alunos'][ra_aluno]['turmas'].append(id_turma)
                        print(f'Aluno com RA {ra_aluno} inserido na turma {id_turma}.')
                    else:
                        print(f'Aluno com RA {ra_aluno} não encontrado.')

            # Opção de salvar a turma e encerrar
            salvar_turma = input('Deseja apenas salvar a turma? (S/N): ')
            if salvar_turma.lower() == 's':
                with open('dados.json', 'w') as arquivo_json:
                    json.dump(dados, arquivo_json, indent=4)
                print('Turma salva com sucesso.')
                return True
