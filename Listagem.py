import json


def listar_turmas(dados):
    print("Turmas presentes:")
    for turma_id, turma_info in dados.get("turmas", {}).items():
        print(f"ID da Turma: {turma_id}")
        print(f"Nome da Turma: {turma_info['nome']}")
        print("-" * 20)

def listar_ciclos(dados):
    print("Ciclos existentes:")
    for ciclo_id, ciclo_info in dados["ciclos"].items():
        print(f"ID do Ciclo: {ciclo_id}")
        print(f"Nome do Ciclo: {ciclo_info['nome']}")
        print("-" * 20)
def listar_grupos(dados):
    print("Grupos presentes:")
    for grupo_id, grupo_info in dados.get("grupos", {}).items():
        print(f"ID do Grupo: {grupo_id}")
        print(f"Nome do Grupo: {grupo_info['nome']}")
        print("Alunos no Grupo:")
        for aluno_id in grupo_info.get("alunos", []):
            aluno_info = dados["alunos"].get(aluno_id, {})
            print(f"- Nome: {aluno_info.get('nome', 'N/A')}, RA: {aluno_info.get('ra', 'N/A')}")
        print("-" * 20)
def listar_alunos(dados):
    print("Alunos presentes:")
    for aluno_id, aluno_info in dados.get("alunos", {}).items():
        print(f"ID do Aluno: {aluno_id}")
        print(f"Nome do Aluno: {aluno_info['nome']}")
        print("-" * 20)
        
def listar_notas(dados):
    print("Notas presentes:")
    for nota_id, nota_info in dados.get("notas", {}).items():
        aluno_info = dados["alunos"].get(nota_info.get("aluno_ra", ""), {})
        ciclo_info = dados["ciclos"].get(nota_info.get("ciclo_id", ""), {})
        turma_info = dados["turmas"].get(nota_info.get("turma_id", ""), {})

        print(f"ID da Nota: {nota_id}")
        print(f"Aluno: {aluno_info.get('nome', 'N/A')} (RA: {aluno_info.get('ra', 'N/A')})")
        print(f"Ciclo: {ciclo_info.get('nome', 'N/A')}")
        print(f"Turma: {turma_info.get('nome', 'N/A')}")
        print(f"Score: {nota_info.get('score', 'N/A')}")
        print("-" * 20)

def listar_alunos_turma(dados, turma):
    if 'alunos' in turma and isinstance(turma['alunos'], list):
        print("\nLista de Alunos:")
        for ra in turma['alunos']:
            if ra in dados['alunos']:
                aluno = dados['alunos'][ra]
                print(f"RA: {ra}, Nome: {aluno['nome']}")
        print("\n")
    else:
        print("Nenhum aluno cadastrado nesta turma.\n")