import matplotlib.pyplot as plt
import json

def grafico1funcao():
    # Carregar os dados do arquivo JSON
    with open('dados.json', 'r') as json_file:
        dados = json.load(json_file)

    # Extrair as notas dos alunos nos ciclos
    alunos = dados['alunos']
    ciclos = dados['ciclos']
    notas = dados['notas']

    # Criar um dicionário para armazenar as notas de cada aluno em cada ciclo
    notas_por_aluno_ciclo = {}

    # Inicializar o dicionário para cada aluno
    for aluno_id, aluno_info in alunos.items():
        notas_por_aluno_ciclo[aluno_info['nome']] = {ciclo['nome']: 0 for ciclo_id, ciclo in ciclos.items()}

    # Preencher o dicionário com as notas reais
    for nota_id, nota_info in notas.items():
        aluno_id = nota_info['aluno_ra']
        ciclo_id = nota_info['ciclo_id']
        score = nota_info['score']

        aluno_nome = alunos[aluno_id]['nome']
        ciclo_nome = ciclos[ciclo_id]['nome']

        notas_por_aluno_ciclo[aluno_nome][ciclo_nome] = score

    # Criar gráfico de barras das notas por aluno nos ciclos
    alunos = list(notas_por_aluno_ciclo.keys())
    ciclos = list(notas_por_aluno_ciclo[alunos[0]].keys())

    for i, aluno in enumerate(alunos):
        scores_aluno = [notas_por_aluno_ciclo[aluno][ciclo] for ciclo in ciclos]
        plt.bar([j + i * 0.2 for j in range(len(ciclos))], scores_aluno, width=0.2, label=aluno)

    plt.xlabel('Ciclos')
    plt.ylabel('Notas')
    plt.title('Notas dos Alunos nos Ciclos')
    plt.legend()
    plt.xticks([i + 0.2 for i in range(len(ciclos))], ciclos, rotation=45)
    plt.tight_layout()

    # Salvar o gráfico como um arquivo de imagem (por exemplo, PNG)
    plt.savefig('notas_alunos_ciclos.png')
    plt.show()
