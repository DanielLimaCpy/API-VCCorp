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

    notas_por_aluno = {aluno['nome']: [] for aluno_id, aluno in alunos.items()}

    for nota_id, nota_info in notas.items():
        aluno_id = nota_info['aluno_ra']
        ciclo_id = nota_info['ciclo_id']
        score = nota_info['score']

        aluno_nome = alunos[aluno_id]['nome']
        ciclo_nome = ciclos[ciclo_id]['nome']

        notas_por_aluno[aluno_nome].append((ciclo_nome, score))

    # Criar gráfico de barras das notas por aluno nos ciclos
    for aluno, notas_ciclos in notas_por_aluno.items():
        if notas_ciclos:  # Verificar se há notas para o aluno
            ciclos_aluno, scores_aluno = zip(*notas_ciclos)
            plt.bar(ciclos_aluno, scores_aluno, label=aluno)

    plt.xlabel('Ciclos')
    plt.ylabel('Notas')
    plt.title('Notas dos Alunos nos Ciclos')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Salvar o gráfico como um arquivo de imagem (por exemplo, PNG)
    plt.savefig('notas_alunos_ciclos.png')
    plt.show()
