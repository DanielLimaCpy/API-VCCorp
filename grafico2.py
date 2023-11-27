import matplotlib.pyplot as plt
import json

def grafico_linhas_progressao_desempenho():
    # Carregar os dados do arquivo JSON
    with open('dados.json', 'r') as json_file:
        dados = json.load(json_file)

    # Extrair as notas dos alunos nos ciclos
    alunos = dados['alunos']
    ciclos = dados['ciclos']
    notas = dados['notas']

    notas_por_aluno = {aluno['nome']: {ciclo['nome']: [] for ciclo_id, ciclo in ciclos.items()} for aluno_id, aluno in alunos.items()}

    for nota_id, nota_info in notas.items():
        aluno_id = nota_info['aluno_ra']
        ciclo_id = nota_info['ciclo_id']
        score = nota_info['score']

        aluno_nome = alunos[aluno_id]['nome']
        ciclo_nome = ciclos[ciclo_id]['nome']

        notas_por_aluno[aluno_nome][ciclo_nome].append(score)

    # Criar gráfico de linhas da progressão de notas por aluno nos ciclos
    for aluno, notas_ciclos in notas_por_aluno.items():
        for ciclo, notas in notas_ciclos.items():
            plt.plot(range(1, len(notas) + 1), notas, marker='o', label=f"{aluno} - {ciclo}")

    plt.xlabel('Ciclos')
    plt.ylabel('Notas')
    plt.title('Progressão de Notas dos Alunos nos Ciclos')
    plt.legend()
    plt.xticks(range(1, len(ciclos) + 1), [ciclo['nome'] for ciclo_id, ciclo in ciclos.items()], rotation=45)
    plt.tight_layout()

    # Salvar o gráfico como um arquivo de imagem (por exemplo, PNG)
    plt.savefig('progressao_notas_alunos_ciclos.png')
    plt.show()
