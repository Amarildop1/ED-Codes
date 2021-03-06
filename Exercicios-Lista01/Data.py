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
hoje = Data(19, 5, 2020)
print("Feito em:", hoje)

data1 = Data(1, 1, 2020)
print("\n", data1)

data2 = Data(21, 4, 2020)
print(data2)


print("\n--- Alteradas ---\n")
# Alterando data1 com o método seter
data1.set_dia(25)
data1.set_mes(6)
data1.set_ano(2021)
print(data1)

# Alterando data2 com o método seter
data2.set_dia(31)
data2.set_mes(10)
data2.set_ano(2022)
print(data2, "\n")
