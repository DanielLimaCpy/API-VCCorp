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
    return dados  # Retorna todos os dados do JSON

# Função para verificar se um ciclo já existe nos dados
def ciclo_existe(id_ciclo, dados):
    return id_ciclo in dados['ciclos']

# Função para editar ciclos
def editar_ciclo():
    dados = carregar_dados()
    id_ciclo = input('Informe o ID do ciclo que deseja editar: ')
    if not ciclo_existe(id_ciclo, dados):
        print(f'O ciclo com o ID {id_ciclo} não está cadastrado.')
        return False

    ciclo = dados['ciclos'][id_ciclo]

    print(f'Editando o ciclo com ID {id_ciclo}. Deixe em branco se não deseja fazer alterações.')

    novo_nome = input(f'Novo Nome ({ciclo["nome"]}): ')
    if novo_nome:
        ciclo['nome'] = novo_nome

    nova_data_inicio = input(f'Nova Data de Início ({ciclo["data_de_inicio"]}): ')
    if nova_data_inicio:
        ciclo['data_de_inicio'] = nova_data_inicio

    nova_data_fim = input(f'Nova Data de Fim ({ciclo["data_de_fim"]}): ')
    if nova_data_fim:
        ciclo['data_de_fim'] = nova_data_fim

    novo_peso = input(f'Novo Peso da Nota ({ciclo["peso_da_nota"]}): ')
    if novo_peso:
        ciclo['peso_da_nota'] = novo_peso

    with open('dados.json', 'w') as arquivo_json:
        json.dump(dados, arquivo_json, indent=4)
    print(f'Dados do ciclo com ID {id_ciclo} foram atualizados com sucesso.')
    return True

# O restante do código permanece igual

  
