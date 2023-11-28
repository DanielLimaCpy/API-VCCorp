import json
from listagem import listar_alunos
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

def calcular_media_ponderada():
    while True:
        dados = carregar_dados()
        notas = dados.get('notas', {})
        listar_alunos(dados)
        aluno_escolhido = input("Digite o ID do aluno para calcular a média ponderada (digite '0' para sair): ")

        if aluno_escolhido == '0':
            print("Saindo do programa.")
            break

        if aluno_escolhido not in dados['alunos']:
            print(f"ERRO: Aluno com ID {aluno_escolhido} não encontrado nos dados.")
            continue
    
        media_por_aluno = {}
    
        for nota_id, nota in notas.items():
            aluno_ra = nota['aluno_ra']
            ciclo_id = nota['ciclo_id']
            score = nota['score']
            peso_ciclo = dados['ciclos'][ciclo_id]['peso_da_nota']
    
            if aluno_ra != aluno_escolhido:
                continue
    
            if aluno_ra not in media_por_aluno:
                media_por_aluno[aluno_ra] = {'total_score': 0, 'total_peso': 0}
    
            media_por_aluno[aluno_ra]['total_score'] += float(score) * float(peso_ciclo)
            media_por_aluno[aluno_ra]['total_peso'] += float(peso_ciclo)
    
        for aluno_ra, media_info in media_por_aluno.items():
            total_score = media_info['total_score']
            total_peso = media_info['total_peso']
            
            if total_peso == 0:
                media_final = 0
            else:
                media_final = total_score / total_peso
            
            # Adiciona a média ponderada (fee) aos dados do aluno sem apagar as informações anteriores
            if aluno_ra == aluno_escolhido:
                dados['alunos'][aluno_ra].setdefault('fee', []).append(round(media_final, 2))
    
        # Remove os totais de score e peso do JSON
        for aluno in dados['alunos'].values():
            aluno.pop('total_score', None)
            aluno.pop('total_peso', None)
    
        # Salva os dados atualizados no mesmo arquivo JSON
        with open('dados.json', 'w') as arquivo_json:
            json.dump(dados, arquivo_json, indent=4)
        
        print(f"Médias calculadas e salvas para o aluno com ID {aluno_escolhido}")
    
        opcao = input("Deseja calcular as médias de outros alunos? (s/n): ").lower()
        if opcao != 's':
            break
