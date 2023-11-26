import json
from editar_alunos import editar_aluno

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

# Função para verificar se um RA de aluno já existe nos dados
def ra_aluno_existe(ra, dados_alunos):
    return ra in dados_alunos['alunos']

# Função para registrar alunos
def func_cadastrar_alunos():
    dados_alunos = carregar_dados_alunos()
    while True:
        ra_aluno = input('Informe o RA do aluno a ser cadastrado: ')

        while True:
            nome_aluno = input('Qual nome do aluno a ser cadastrado? ')
            if nome_aluno.isalpha() and len(nome_aluno) <= 70:
                break
            else:
                print('Nome inválido, escreva apenas com letras')

        while True:
            idade_aluno = input('Qual idade do aluno a ser cadastrado? ')
            if idade_aluno.isdigit() and int(idade_aluno) <= 130:
                break
            else:
                print('Idade inválida, escreva apenas com números')

        while True:
            email_aluno = input('Qual e-mail do aluno a ser cadastrado? ')
            
            if '@' and '.' in email_aluno:
                break
            else:
                print('E-mail inválido, escreva novamente')
        
        novo_aluno = {
            'ra': ra_aluno,
            'nome': nome_aluno,
            'idade': idade_aluno,
            'email': email_aluno,
            'turmas': [],
            'grupos': []
        }

        while True:
            # Exibir dados do aluno para confirmação e opções
            print(f'\n\n\nRA: {ra_aluno}')
            print(f'Nome: {nome_aluno}')
            print(f'Idade: {idade_aluno}')
            print(f'E-mail: {email_aluno}')

            menu_cad_aluno_1 = input('Para confirmar, escolha a opção:\n1-Alterar Nome\n2-Alterar Idade\n3-Alterar E-mail\n4-Salvar e cadastrar outro aluno\n5-Confirmar cadastro e voltar ao menu\n6-Cancelar cadastro e voltar ao menu\n')

            if menu_cad_aluno_1 == '1':
                nome_aluno = input('Novo Nome: ')
            elif menu_cad_aluno_1 == '2':
                idade_aluno = input('Nova Idade: ')
            elif menu_cad_aluno_1 == '3':
                email_aluno = input('Novo E-mail: ')
            elif menu_cad_aluno_1 == '4':

                # Salva os dados do aluno atual e permite cadastrar outro aluno
                dados_alunos['alunos'][ra_aluno] = novo_aluno
                with open('dados.json', 'w') as arquivo_dados_alunos_json:
                    json.dump(dados_alunos, arquivo_dados_alunos_json, indent=4)
                print('Cadastro realizado com sucesso. Continuando com o próximo aluno.')
                break  # Sai do loop interno e permite cadastrar outro aluno

            elif menu_cad_aluno_1 == '5':
                dados_alunos['alunos'][ra_aluno] = novo_aluno
                with open('dados.json', 'w') as arquivo_dados_alunos_json:
                    json.dump(dados_alunos, arquivo_dados_alunos_json, indent=4)
                print('Cadastro realizado com sucesso.')
                return True
            
            elif menu_cad_aluno_1 == '6':
                print('Cadastro cancelado.')
                return False
