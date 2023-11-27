import json
from editar_ciclos import editar_ciclo
from datetime import datetime
from validacao_data import obter_data_inicio
import random

def default_serializer(obj):
    if isinstance(obj, datetime):
        return obj.strftime("%d/%m/%Y")

def gerar_id_aleatorio():
    id_prefixo = "c"
    id_numero_aleatorio = ''.join([str(random.randint(0, 9)) for _ in range(7)])
    return f"{id_prefixo}{id_numero_aleatorio}"

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

# Função para verificar se um ciclo já existe nos dados
def ciclo_existe(id_ciclo, dados):
    return id_ciclo in dados['ciclos']

# Função para cadastrar ciclos
def func_cadastrar_ciclos():
    while True:
        dados = carregar_dados()

        # Pergunta em qual turma deseja acrescentar um ciclo
        id_turma = input('Informe o ID da turma em que deseja adicionar um ciclo (0 para voltar): ')

        if id_turma == '0':
            break

        # Verifica se a turma existe nos dados
        if id_turma not in dados['turmas']:
            print('A turma com este ID não existe. Crie a turma antes de vincular o ciclo.')
            continue

        # Verifica se a turma já tem ciclos
        if 'ciclos' in dados['turmas'][id_turma]:
            print('Ciclos já vinculados à turma:')
            for ciclo in dados['turmas'][id_turma]['ciclos']:
                print(f'ID: {ciclo["id"]}, Nome: {ciclo["nome"]}')
        else:
            print('A turma ainda não possui ciclos vinculados.')

        id_ciclo = gerar_id_aleatorio()

        if id_ciclo == '0':
            break

        # Verifica se o ciclo já existe nos dados
        if ciclo_existe(id_ciclo, dados):
            print('O ciclo com este ID já está cadastrado.')
            opcao = input('O que deseja fazer?\n1 - Criar um novo ciclo\n2 - Editar os dados do ciclo\n')

            if opcao == '1':
                continue
            elif opcao == '2':
                if editar_ciclo(id_ciclo, dados):
                    print('Edição do ciclo realizada com sucesso.')
                else:
                    print('Edição do ciclo cancelada.')
                break

        nome_ciclo = input('Qual o nome do ciclo? ')
        while True:
            datacheck = input('Qual a data de início do ciclo? (formato: dd/mm/aaaa) ')
            data_inicio = obter_data_inicio(datacheck)

            if data_inicio is not None:
                break  # Saia do loop interno se a data for válida
            else:
                print('insira uma data valida')
        print(data_inicio.strftime('%d/%m/%Y'))
        
        while True:
            try:
                datafim = input('Qual a data do fim do ciclo? (formato: dd/mm/aaaa) ')
                data_fim = datetime.strptime(datafim, "%d/%m/%Y")
                if data_fim >= data_inicio:
                    break  # Saia do loop interno se a data for válida
                else:
                    print("A data inserida não pode ser anterior à data inicial.")
            except ValueError:
                print("Formato de data inválido. Tente novamente.")

        print(data_fim.strftime('%d/%m/%Y'))

    
        while True:
            peso_nota = input('Qual o peso da nota do ciclo? ')
            if peso_nota.isdigit():
                break
            else:
                print('Peso inválido, o peso tem que ser em números')

        novo_ciclo = {
            'id': id_ciclo,
            'nome': nome_ciclo,
            'data_de_inicio': data_inicio,
            'data_de_fim': data_fim,
            'peso_da_nota': peso_nota,
        }

        # Adiciona o ciclo à lista de ciclos da turma
        if 'ciclos' not in dados['turmas'][id_turma]:
            dados['turmas'][id_turma]['ciclos'] = []

        dados['turmas'][id_turma]['ciclos'].append(novo_ciclo)
        dados['ciclos'][id_ciclo] = novo_ciclo

        with open('dados.json', 'w') as arquivo_json:
            json.dump(dados, arquivo_json, indent=4, default=default_serializer)

        print('Cadastro do ciclo realizado com sucesso e vinculado à turma.')
        break

func_cadastrar_ciclos()
