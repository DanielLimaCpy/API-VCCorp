import json


def carregar_dados():
    try:
        with open('dados.json', 'r') as arquivo_dados_alunos_json:
            dados_alunos = json.load(arquivo_dados_alunos_json)
    except FileNotFoundError:
        # Se o arquivo não existir, cria uma estrutura vazia
        dados_alunos = {
            "alunos": {},
            "turmas": {},
            "ciclos": {},
            "grupos": {},
            "notas": {}
        }
    return dados_alunos

def editar_nota():
    dados = carregar_dados()

    nota_id = input("Digite o ID da nota que deseja editar: ")

    if nota_id in dados['notas']:
        nota = dados['notas'][nota_id]
        print(f'Editando nota com ID: {nota_id}')
        while True:
            print(f' Aluno: {dados["alunos"].get(nota["aluno_ra"], {}).get("nome")}')
            print(f' Ciclo: {dados["ciclos"].get(nota["ciclo_id"], {}).get("nome")}')
            print(f' Turma: {dados["turmas"].get(nota["turma_id"], {}).get("nome")}')
            print(f' Score: {nota["score"]}')

            campo = input('Escolha o campo que deseja editar alguma nota(S/N)? ').strip().lower()

            if campo == 's':
                nova_nota = float(input('Informe a nova nota: '))
                if 0 <= nova_nota <= 10:
                    nota["score"] = nova_nota
                else:
                    print('Nota inválida. A nota não foi alterada.')

            elif campo == '':
                with open('dados.json', 'w') as arquivo_json:
                    json.dump(dados, arquivo_json, indent=4)
                print('Edição de nota realizada com sucesso.')
                return True

            else:
                print('Opção inválida. Tente novamente.')

    else:
        print(f'A nota com ID {nota_id} não foi encontrada.')
        return False
