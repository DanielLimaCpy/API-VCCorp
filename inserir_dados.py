import json
import random
from faker import Faker
from tqdm import tqdm

fake = Faker('pt_BR')

with open('dados.json', 'r+') as json_file:
    dados = json.load(json_file)

alunos = dados['alunos']

for aluno_id in alunos:
    alunos[aluno_id]['f.e.e'] = ""

for i in tqdm(range(100), desc='Gerando informações aleatórias para alunos'):
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

grupos = dados.get('grupos', {})
turmas = dados.get('turmas', {})
ciclos = dados.get('ciclos', {})

for i in tqdm(range(1, 101), desc='Adicionando grupos'):
    novo_grupo = {
        "id": f"G{i}",
        "nome": f"Grupo {chr(65 + (i % 26))}",
        "alunos": [f"{j}" for j in range(1, 31)]
    }
    grupos[str(len(grupos) + 1)] = novo_grupo

for i in tqdm(range(1, 101), desc='Adicionando turmas e ciclos'):
    alunos_turma = [f"ra{random.randint(1000000, 9999999)}" for _ in range(random.randint(5, 15))]

    nova_turma = {
        "id": f"T{i:07}",
        "nome": f"Turma {i}",
        "data_de_inicio": f"2023-{i % 12 + 1:02}-01",
        "ciclos": [f"{len(ciclos) + 1}"],
        "alunos": alunos_turma
    }
    turmas[f"{len(turmas) + 1}"] = nova_turma

    novo_ciclo = {
        "id": f"C{i:07}",
        "nome": f"Prova {i}",
        "data_de_inicio": f"2023-{i % 12 + 1:02}-01",
        "data_de_fim": f"2023-{i % 12 + 1:02}-28",
        "peso_da_nota": f"{random.randint(1, 5)}"
    }
    ciclos[f"{len(ciclos) + 1}"] = novo_ciclo

notas = dados.get('notas', {})

for i in tqdm(range(1, 101), desc='Adicionando notas'):
    nova_nota = {
        "aluno_ra": f"ra{random.randint(1000000, 9999999)}",
        "ciclo_id": f"{random.randint(1, len(ciclos))}",
        "turma_id": f"{random.randint(1, len(turmas))}",
        "score": round(random.uniform(0, 10), 1)
    }
    notas[f"N{i:07}"] = nova_nota

dados['grupos'] = grupos
dados['turmas'] = turmas
dados['ciclos'] = ciclos
dados['notas'] = notas

with open('dados.json', 'w') as json_file:
    json.dump(dados, json_file, indent=4)
