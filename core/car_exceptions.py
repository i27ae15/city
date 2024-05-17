
class CarroApagadoError(Exception):

    def __init__(self, *args, **kargs) -> None:
        self.mensaje: str = 'EL CARRO ESTA ESTA APAGADO'
        super().__init__(self.mensaje)


class NoHayGasolina(Exception):

    def __init__(self, *args, **kargs) -> None:
        self.mensaje: str = 'ELCARRO NO POSEE GASOLINA'
        super().__init__(self.mensaje)


class AceleracionMaximaSobrepasada(Exception):
    def __init__(self, *args: object) -> None:
        self.mensaje = "LA ACELERACION MAXIMA FUE SOBREPASADA"
        super().__init__(self.mensaje)


class MotorInexistente(Exception):
    def __init__(self, *args: object) -> None:
        self.mensaje = "EL CARRO NO POSEE MOTOR"
        super().__init__(*args)


class RuedasExistente(Exception):
    def __init__(self, *args: object) -> None:
        self.name = "YA EL CARRO POSEE RUEDAS"
        super().__init__(self.name)


class CarroConVelocidad(Exception):
    def __init__(self, *args: object) -> None:
        self.name = "EL CARRO NO DEBE TENER VELOCIDAD"
        super().__init__(self.name)
