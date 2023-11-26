import json
from editar_grupos import editar_grupo
from editar_alunos import editar_aluno 


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


def func_cadastrar_grupos():
    dados = carregar_dados()
    while True:
        grupo_id = input('Informe o ID do grupo a ser cadastrado: ')
        if grupo_id in dados['grupos']:
            print('O ID já está cadastrado. O que deseja fazer?')
            opcao = input('1 - Criar um novo grupo\n2 - Editar os dados do grupo\n')
            if opcao == '1':
                continue
            elif opcao == '2':
                editar_grupo(grupo_id, dados)
                return False
        else:
            nome_grupo = input('Qual o nome do grupo? ')
            alunos_grupo = []  # Lista para armazenar os RAs dos alunos

            while True:
                ra_aluno = input('Informe o RA de um aluno (ou deixe em branco para encerrar): ')
                if not ra_aluno:
                    break
                if ra_aluno not in dados['alunos']:
                    print(f"O aluno com RA {ra_aluno} não existe no sistema.")
                    opcao = input('1 - Continuar mesmo assim\n2 - Cancelar cadastro\n')
                    if opcao == '2':
                        continue
                alunos_grupo.append(ra_aluno)

            # Adicione outros campos relevantes
            novo_grupo = {
                'id': grupo_id,
                'nome': nome_grupo,
                'alunos': alunos_grupo,  # Adicione os RAs dos alunos ao grupo
                # Adicione outros campos relevantes
            }

            dados['grupos'][grupo_id] = novo_grupo
            with open('dados.json', 'w') as arquivo_json:
                json.dump(dados, arquivo_json, indent=4)
            print('Cadastro do grupo realizado com sucesso.')
            return True