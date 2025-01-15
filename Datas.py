#Carregue a data atual do computador e, com base na data atual, apresente a data de dois dias no futuro

from datetime import datetime, timedelta

agora = datetime.now()
print(f"Data de hj: {agora}")
data_futura=agora + timedelta(2)
print(f"Data dois dias depois: {data_futura}")


#Carregue a data atual do computador e apresente somente a data

atual = datetime.now()

print(f"Somente a data: {atual.date()}")