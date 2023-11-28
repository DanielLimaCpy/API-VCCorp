import pandas as pd
import json
# Carregar o JSON a partir do arquivo
with open('dados.json', 'r') as file:
    seu_json = json.load(file)

# Função para extrair informações do JSON e organizar em um DataFrame
def extrair_dados(json_data):
    alunos_data = []
    turmas_data = []
    ciclos_data = []
    grupos_data = []
    notas_data = []

    for aluno_id, aluno_info in json_data["alunos"].items():
        aluno_data = {"ID": aluno_id}
        aluno_data.update(aluno_info)
        alunos_data.append(aluno_data)

    for turma_id, turma_info in json_data["turmas"].items():
        turma_data = {"ID": turma_id}
        turma_data.update(turma_info)
        turmas_data.append(turma_data)

        for ciclo_info in turma_info.get("ciclos", []):
            ciclo_data = {"ID": ciclo_info["id"]}
            ciclo_data.update(ciclo_info)
            ciclos_data.append(ciclo_data)

    for grupo_id, grupo_info in json_data["grupos"].items():
        grupo_data = {"ID": grupo_id}
        grupo_data.update(grupo_info)
        grupos_data.append(grupo_data)

    for nota_id, nota_info in json_data["notas"].items():
        nota_data = {"ID": nota_id}
        nota_data.update(nota_info)
        notas_data.append(nota_data)

    alunos_df = pd.DataFrame(alunos_data)
    turmas_df = pd.DataFrame(turmas_data)
    ciclos_df = pd.DataFrame(ciclos_data)
    grupos_df = pd.DataFrame(grupos_data)
    notas_df = pd.DataFrame(notas_data)

    return alunos_df, turmas_df, ciclos_df, grupos_df, notas_df

# Extrair dados do JSON
alunos_df, turmas_df, ciclos_df, grupos_df, notas_df = extrair_dados(seu_json)

# Salvar os DataFrames em arquivos Excel
with pd.ExcelWriter('dados.xlsx', engine='openpyxl') as writer:
    alunos_df.to_excel(writer, sheet_name='Alunos', index=False)
    turmas_df.to_excel(writer, sheet_name='Turmas', index=False)
    ciclos_df.to_excel(writer, sheet_name='Ciclos', index=False)
    grupos_df.to_excel(writer, sheet_name='Grupos', index=False)
    notas_df.to_excel(writer, sheet_name='Notas', index=False)



