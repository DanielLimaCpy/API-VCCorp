from datetime import datetime

def obter_data_inicio(dataini):
    while True:
        try:
            # Modifique o formato para "%d/%m/%Y" para aceitar data no formato dd/mm/aaaa
            datain = datetime.strptime(dataini, "%d/%m/%Y")

            if datain >= datetime.now():
                return datain
            else:
                print("A data inserida não pode ser anterior à data atual.")
        except ValueError:
            print("Formato de data inválido. Tente novamente.")
            return None

def obter_data_fim(datafim, datain):
    while True:
        try:
            # Modifique o formato para "%d/%m/%Y" para aceitar data no formato dd/mm/aaaa
            datafi = datetime.strptime(datafim, "%d/%m/%Y")

            if datafi >= datain:
                return datafi
            else:
                print("A data inserida não pode ser anterior à data inicial.")
        except ValueError:
            print("Formato de data inválido. Tente novamente.")
            return None

