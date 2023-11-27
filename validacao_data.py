from datetime import datetime

datain = None  # Inicialize a variável global

def obter_data_inicio(dataini):
    global datain
    while True:
        try:
            datain = datetime.strptime(dataini, "%d/%m/%Y")
            if datain >= datetime.now():
                return datain
            else:
                print("A data inserida não pode ser anterior à data atual.")
        except ValueError:
            print("Formato de data inválido. Tente novamente.")
            return None
       