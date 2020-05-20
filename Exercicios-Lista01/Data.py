# ED com Python
# Exercício de Fixação
# L01 - Q01

class Data:
    def __init__(self, dia, mes, ano):
        self._dia = dia
        self._mes = mes
        self._ano = ano
    
    def get_dia():
        return _dia
    
    def set_dia(self, d):
        self._dia = d

    def get_mes():
        return self._mes

    def set_mes(self, m):
        self._dia = m

    def get_ano():
        return self._ano
    
    def set_ano(self, a):
        self._dia = a


    def __str__(self):
        return f"{self._dia}/{self._mes}/{self._ano}"


# Programa Principal
data1 = Data(1, 1, 2020)
data2 = Data(19, 5, 2020)

print(data1)
print(data2)