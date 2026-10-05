# O - Open/Closed Principle
# Abierto/Cerrado

class Descuento:
    def aplicar(self, precio):
        return precio


class DescuentoVIP(Descuento):
    def aplicar(self, precio):
        return precio * 0.8


class DescuentoEstudiante(Descuento):
    def aplicar(self, precio):
        return precio * 0.9


precio = 100

print("Precio con descuento VIP:", DescuentoVIP().aplicar(precio))
print("Precio con descuento estudiante:", DescuentoEstudiante().aplicar(precio))
