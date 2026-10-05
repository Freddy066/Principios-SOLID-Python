# I - Interface Segregation Principle
# Segregación de Interfaces

from abc import ABC, abstractmethod


class Impresora(ABC):
    @abstractmethod
    def imprimir(self):
        pass


class Escaner(ABC):
    @abstractmethod
    def escanear(self):
        pass


class ImpresoraSencilla(Impresora):
    def imprimir(self):
        print("Imprimiendo documento...")


impresora = ImpresoraSencilla()
impresora.imprimir()
