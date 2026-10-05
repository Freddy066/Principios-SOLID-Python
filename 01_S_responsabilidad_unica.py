# S - Single Responsibility Principle
# Responsabilidad Única

class Reporte:
    def __init__(self, contenido):
        self.contenido = contenido


class GuardadorReporte:
    def guardar(self, reporte: Reporte, ruta: str):
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(reporte.contenido)


reporte = Reporte("Reporte generado correctamente.")
guardador = GuardadorReporte()
guardador.guardar(reporte, "reporte.txt")

print("Reporte creado y guardado correctamente.")
