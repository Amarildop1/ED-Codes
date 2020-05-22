# FALTA Finalizar

# ED com Python
# Exercício de Fixação
# L01 - Q02

class Aluno:
    def __init__(self, matricula, nome, notas):
        self.__matricula = matricula
        self.__nome = nome
        self.__notas = notas

    def get_matricula(self):
        return f"Matricula: {self.__matricula}"

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_notas(self):
        return self.__notas
 

#--- Main ---
a1 = Aluno(12345, "Fred", [100, 90, 80])

print(a1.get_nome())
print(a1.get_matricula())
print(a1.get_notas())

