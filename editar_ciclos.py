import json
from datetime import datetime
from validacao_data import obter_data_inicio

def default_serializer(obj):
    if isinstance(obj, datetime):
        return obj.strftime("%d/%m/%Y")

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
    return dados  # Retorna todos os dados do JSON

def listar_ciclos(dados):
    print("Ciclos existentes:")
    for ciclo_id, ciclo_info in dados["ciclos"].items():
        print(f"ID do Ciclo: {ciclo_id}")
        print(f"Nome do Ciclo: {ciclo_info['nome']}")
        print("-" * 20)

# Função para verificar se um ciclo já existe nos dados
def ciclo_existe(id_ciclo, dados):
    return id_ciclo in dados['ciclos']

# Função para editar ciclos
def editar_ciclo():
    dados = carregar_dados()
    listar_ciclos(dados)
    id_ciclo = input('Informe o ID do ciclo que deseja editar: ')
    if not ciclo_existe(id_ciclo, dados):
        print(f'O ciclo com o ID {id_ciclo} não está cadastrado.')
        return False

    ciclo = dados['ciclos'][id_ciclo]

    print(f'Editando o ciclo com ID {id_ciclo}. Deixe em branco se não deseja fazer alterações.')

    novo_nome = input(f'Novo Nome ({ciclo["nome"]}): ')
    if novo_nome:
        ciclo['nome'] = novo_nome

    while True:
        nova_data_inicio = input(f'Nova Data de Início ({ciclo["data_de_inicio"]}): ')

        # Saia do loop se o usuário inserir 0
        if nova_data_inicio == '':
            break

        datacheck = nova_data_inicio
        try:
            data_inicio = obter_data_inicio(datacheck)
            if data_inicio is not None:
                break  # Saia do loop interno se a data for válida
        except ValueError:
            print("Formato de data inválido. Tente novamente.")

    # Se o usuário inserir 0, não atualize o ciclo['data_de_inicio']
    if nova_data_inicio != '':
        ciclo['data_de_inicio'] = nova_data_inicio

    while True:
        nova_data_fim = input(f'Nova Data de Fim ({ciclo["data_de_fim"]}): ')

        # Saia do loop se o usuário inserir 0
        if nova_data_fim == '':
            break

        data_fim = datetime.strptime(nova_data_fim, "%d/%m/%Y")
        try:
            data_inicio= datetime.strptime(ciclo["data_de_inicio"], "%d/%m/%Y")
            if data_fim >= data_inicio:
                break  # Saia do loop interno se a data for válida
            else:
                print("A data inserida não pode ser anterior à data inicial.")
        except ValueError:
            print("Formato de data inválido. Tente novamente.")
       
    if nova_data_fim !='':
        ciclo['data_de_fim'] = nova_data_fim

    novo_peso = input(f'Novo Peso da Nota ({ciclo["peso_da_nota"]}): ')
    if novo_peso:
        ciclo['peso_da_nota'] = novo_peso

    with open('dados.json', 'w') as arquivo_json:
        json.dump(dados, arquivo_json, indent=4, default=default_serializer)
    print(f'Dados do ciclo com ID {id_ciclo} foram atualizados com sucesso.')
    return True

# O restante do código permanece igual


