# L - Liskov Substitution Principle
# Sustitución de Liskov

class Ave:
    pass


class AveVoladora(Ave):
    def volar(self):
        return "Volando..."


class Pinguino(Ave):
    def nadar(self):
        return "Nadando..."


ave = AveVoladora()
pinguino = Pinguino()

print(ave.volar())
print(pinguino.nadar())
