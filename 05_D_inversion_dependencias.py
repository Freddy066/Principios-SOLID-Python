# D - Dependency Inversion Principle
# Inversión de Dependencias

from abc import ABC, abstractmethod


class ServicioMensaje(ABC):
    @abstractmethod
    def enviar(self, msg):
        pass


class ServicioSMS(ServicioMensaje):
    def enviar(self, msg):
        print(f"SMS: {msg}")


class ServicioEmail(ServicioMensaje):
    def enviar(self, msg):
        print(f"Email: {msg}")


class Notificador:
    def __init__(self, servicio: ServicioMensaje):
        self.servicio = servicio

    def enviar_alerta(self, msg):
        self.servicio.enviar(msg)


notificador_sms = Notificador(ServicioSMS())
notificador_sms.enviar_alerta("Alerta por SMS")

notificador_email = Notificador(ServicioEmail())
notificador_email.enviar_alerta("Alerta por Email")
