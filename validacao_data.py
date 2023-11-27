from datetime import datetime, date

def obter_data_inicio(datacheck):
    while True:
        try:
            datachk = datetime.strptime(datacheck, "%d/%m/%Y")
            
            return datachk  # Retorna a data se a conversão for bem-sucedida
        except ValueError:
            print("Formato de data inválido. Tente novamente.")
            datacheck = input("Nova Data de Início: ")  # Solicita uma nova entrada
