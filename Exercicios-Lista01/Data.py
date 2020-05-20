# ED com Python
# Exercício de Fixação
# L01 - Q01

class Data:
    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
    
    def get_dia():
        return __dia
    
    def set_dia(self, dia):
        self.__dia = dia

    def get_mes():
        return self.__mes

    def set_mes(self, mes):
        self.__mes = mes

    def get_ano():
        return self.__ano
    
    def set_ano(self, ano):
        self.__ano = ano


    def __str__(self):
        return f"{self.__dia}/{self.__mes}/{self.__ano}"

# Programa Principal
data1 = Data(1, 1, 2020)
data2 = Data(19, 5, 2020)

print(data1)
print(data2)


data1.set_dia(31)
data1.set_mes(10)
data1.set_ano(2021)


print("\n--- Alterei ---\n")
print(data1)
