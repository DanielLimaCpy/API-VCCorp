import os
import openpyxl
import json
import random

def ra_aluno_existe(ra, dados_alunos):
    return ra in dados_alunos['alunos']

def gerar_ra_aleatorio():
    return f"Ra{random.randint(1000, 9999)}"  # Gera um número aleatório entre 1000 e 9999

def excel_para_json(nome_arquivo_excel):
    # Carregar o arquivo Excel
    workbook = openpyxl.load_workbook(nome_arquivo_excel)
    sheet = workbook['alunos']  # Substitua 'alunos' pelo nome da sua planilha no arquivo Excel

    # Carregar dados existentes do JSON, se houver
    dados_json = {}
    if os.path.exists('dados.json'):
        with open('dados.json', 'r') as arquivo_json:
            dados_json = json.load(arquivo_json)

    contador = len(dados_json.get('alunos', {})) + 1  # Obter o número atual de alunos no JSON

    for row in sheet.iter_rows(min_row=2, values_only=True):  # Começando da segunda linha, considerando cabeçalhos na primeira
        # Verificar se pelo menos uma célula na linha está preenchida
        if any(value is not None and value != '' for value in row):
            aluno = {
                "ra": gerar_ra_aleatorio(),  # Gerar RA aleatório
                "nome": row[1],
                "idade": str(row[2]),
                "email": row[3],
                "turmas": [],
                "grupos": []
            }
            novo_ra = aluno["ra"]
            while ra_aluno_existe(novo_ra, dados_json):  # Verificar se o RA gerado já existe
                novo_ra = gerar_ra_aleatorio()  # Gerar um novo RA se já existir no JSON
                aluno["ra"] = novo_ra

            dados_json.setdefault("alunos", {})[novo_ra] = aluno  # Adicionar aluno ao JSON com o novo RA

    # Salvar os dados no formato JSON
    with open('dados.json', 'w') as arquivo_json:
        json.dump(dados_json, arquivo_json, indent=4)
        print('Importação salva com sucesso')

# Chamada da função para importar o arquivo Excel e transformar em JSON
def iniciar_importacao():
    nome_arquivo = input('Digite o nome do seu arquivo .xlsx (sem o caminho): ')  # Solicita apenas o nome do arquivo
    nome_arquivo_excel = os.path.join(os.getcwd(), f"{nome_arquivo}.xlsx")  # Adiciona o caminho do diretório atual ao nome do arquivo
    excel_para_json(nome_arquivo_excel)

# Executar a importação
iniciar_importacao()
