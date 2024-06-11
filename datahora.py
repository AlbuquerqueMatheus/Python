from datetime import datetime

data = datetime.now()
data_hora = data.strftime('%d/%m/%Y %H:%M')
print(data_hora)