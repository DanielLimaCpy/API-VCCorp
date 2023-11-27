import json
import random
from faker import Faker

# Criando uma estrutura JSON vazia com a estrutura esperada
dados = {
    "alunos": {}
}

# Salvando a estrutura vazia no arquivo "dados_teste.json"
with open('dados_teste.json', 'w') as json_file:
    json.dump(dados, json_file, indent=4)

print("Estrutura vazia criada com sucesso no arquivo dados_teste.json.")

fake = Faker('pt_BR')

max_iterations = 100
dados_saved = False

with open('dados_teste.json', 'r+') as json_file:
    dados = json.load(json_file)
    alunos = dados.get('alunos', {})

    i = 0
    while i < max_iterations and not dados_saved:
        novo_aluno = {
            "ra": f"ra{random.randint(1000000, 9999999)}",
            "nome": fake.name(),
            "idade": str(random.randint(18, 25)),
            "email": fake.email(),
            "turmas": [],
            "grupos": [],
            "f.e.e": ""
        }
        alunos[str(len(alunos) + 1)] = novo_aluno
        i += 1

    # Update the students' data
    dados['alunos'] = alunos

    # Set the file cursor to the beginning of the file
    json_file.seek(0)

    # Write the updated data to the file
    json.dump(dados, json_file, indent=4)

    # Truncate the file to remove any remaining content
    json_file.truncate()

    # Verificar se os dados foram salvos corretamente
    json_file.seek(0)
    data_in_file = json.load(json_file)
    if data_in_file == dados:
        dados_saved = True
        print(f"Todos os alunos foram criados e salvos corretamente no arquivo dados_teste.json.")
    else:
        print("Houve um problema ao salvar os alunos no arquivo dados_teste.json.")
