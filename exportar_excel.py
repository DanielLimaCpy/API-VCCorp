import pandas as pd
import json

def exportar_para_excel(dados_json, relatorio_excel):
    try:
        with open(dados_json, 'r') as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        print(f'O arquivo {dados_json} não foi encontrado.')
        return

    alunos_df = pd.DataFrame(data.get('Alunos', []))
    turmas_df = pd.DataFrame(data.get('Turmas', []))
    grupos_df = pd.DataFrame(data.get('Grupos_de_alunos', []))
    ciclos_df = pd.DataFrame(data.get('Ciclos', []))
    notas_df = pd.DataFrame(data.get('Notas', []))

    writer = pd.ExcelWriter(relatorio_excel, engine='openpyxl')
    alunos_df.to_excel(writer, sheet_name='Alunos', index=False)
    turmas_df.to_excel(writer, sheet_name='Turmas', index=False)
    grupos_df.to_excel(writer, sheet_name='Grupos_de_alunos', index=False)
    ciclos_df.to_excel(writer, sheet_name='Ciclos', index=False)
    notas_df.to_excel(writer, sheet_name='Notas', index=False)
    writer.save()
    print(f'O arquivo XLSX foi gerado com sucesso: {relatorio_excel}')

if __name__ == "__main__":
    exportar_para_excel('C:\Users\Noite\Documents\GitHub\VCCorp', 'C:\Users\Noite\Documents\GitHub\VCCorp\sprint_3')
