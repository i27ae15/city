from core.car_exceptions import (
    CarroApagadoError, CarroConVelocidad, MotorInexistente, NoHayGasolina,
    RuedasExistente
)

from core.typing import (
    ColorClass, DiccDoor, DiccWheel, MarcasClass, NumDoors

)


class Wheel():
    def __init__(self, marca: MarcasClass, color: ColorClass) -> None:
        self.color: ColorClass = color
        self.marca: MarcasClass = marca


class Door():
    def __init__(self, color: ColorClass) -> None:
        self.color: ColorClass = color


class Engine():
    def __init__(self, marca: str) -> None:
        self.marca: str = marca


class Car():
    def __init__(
        self,
        color: ColorClass,
        marca: MarcasClass,
        modelo: str,
        wheels_info: DiccWheel,
        doors_info: DiccDoor,
        num_doors: NumDoors = NumDoors.n_2.value,
        engine_info: str = None,
        vel_max: int = 200,
        tanq_gaso_max: int = 50
    ) -> None:

        self.color: ColorClass = color
        self.marca: MarcasClass = marca
        self.modelo: str = modelo
        self._wheels_list: list[Wheel] = []
        self.wheels_info: list[dict] = wheels_info
        self.doors_list: list[Door] = []
        self.doors_info: list[dict] = doors_info
        self.num_doors: int = num_doors
        self.engine_info: str = engine_info
        self.motor = None
        self.tanq_cap_max = tanq_gaso_max
        self.tanq_gaso = tanq_gaso_max

        self.encendido: bool = False
        self.vel: int = 0
        self.vel_max: int = vel_max

        self.x: int = 0
        self.y: int = 0
        self.mov_x: bool = False
        self.mov_y: bool = False

        self.new_x: int = 0
        self.new_y: int = 0

        self.max_wheels: int = 4

        self._create_wheels()

    @property
    def estado_del_encendido(self) -> str:
        if self.encendido:
            return 'ENCENDIDO'
        return 'APAGADO'

    @property
    def num_wheels(self) -> int:
        return len(self._wheels_list)

    def _create_wheels(self):

        if self._wheels_list:
            raise RuedasExistente()

        # lista de diccionarios que son la informacion de las ruedas

        for wheel in self.wheels_info:
            marca = wheel['MARCA']
            color = wheel['COLOR']

            self._wheels_list.append(
                Wheel(marca=marca.name, color=color.name)
                )

        can = self.max_wheels - len(self._wheels_list)

        for _ in range(can):
            self._wheels_list.append(
                Wheel(marca=self.marca, color=self.color)
                )

    def create_wheels_for(self):

        if self.wheels_list:
            raise ValueError('YA HAY RUEDAS CREADAS')

        wheels_to_create = self.max_wheels - len(self.wheels_list)

        for i in range(wheels_to_create):
            try:
                wheel = self.wheels_info[i]
            except IndexError:
                wheel = {
                    'MARCA': self.marca,
                    'COLOR': self.color
                }

            marca = wheel['MARCA']
            color = wheel['COLOR']

            self.wheels_list.append(
                Wheel(marca=marca, color=color)
            )

    def create_doors(self):
        if len(self.doors_info) <= self.num_doors:
            for door in self.doors_info:
                color = door['COLOR']
                self.doors_list.append(Door(color=color))

            can = self.num_doors - len(self.doors_list)

            if can > 0:
                for _ in range(can):
                    self.doors_list.append(
                        Door(color=self.color)
                        )
        else:
            raise ValueError(
                f'TIENE QUE HABER {self.num_doors} O MENOS DICC DE PUERTAS'
                )

    def create_engine(self):
        if self.engine_info is None:
            self.motor = Engine(marca=self.marca)
        else:
            self.motor = Engine(marca=self.engine_info)

    def start(self):
        if not isinstance(self.motor, Engine):
            raise MotorInexistente()

        if self.tanq_gaso <= 0:
            raise NoHayGasolina()

        if self.vel != 0:
            raise CarroConVelocidad()

        if self.encendido is True:
            return print('YA EL CARRO ESTA ENCENDIDO')

        self.encendido = (True, 'ENCENDIDO')

    def finish(self):
        if not self.encendido:
            raise CarroApagadoError()
        self.encendido = (False, 'APAGADO')
        self.vel = 0

    def acelerar(self, a: int):

        if not self.encendido:
            raise CarroApagadoError()

        if self.tanq_gaso <= 0:
            raise NoHayGasolina()

        self.vel += a

        if self.vel >= self.vel_max:
            self.vel = self.vel_max

    def frenar(self, a: int):

        if not self.encendido:
            raise CarroApagadoError()

        if self.tanq_gaso <= 0:
            raise NoHayGasolina()

        self.vel -= a

        if self.vel <= 0:
            self.vel = 0

    def gastar_gas(self):

        gas = self.vel

        if self.tanq_gaso == gas:
            self.tanq_gaso = 0
            self.encendido = (False, 'APAGADO')
            self.vel = 0
        else:
            self.tanq_gaso -= gas

    def veri_gas(self):
        gas = self.vel
        tanque = self.tanq_gaso

        if tanque > gas:
            tanque -= gas
            return tanque

        tanque = 0

        return tanque

    def Llenar_gas(self, recarga: int):
        recarga_total = recarga + self.tanq_gaso
        if self.encendido:
            raise ValueError('NO SE PUEDE RECARGAR CON EL CARRO ENCENDIDO')
        if recarga_total > self.tanq_cap_max:
            raise ValueError('LA RECARGA SUPERA LA CANTIDAD DEL TANQUE')
        self.tanq_gaso += recarga_total

    def derecha(self):
        if self.tanq_gaso <= 0:
            raise NoHayGasolina()

        if self.veri_gas() < 0:
            raise ValueError('EL GAS NO ES SUFICIENTE PARA REALIZAR EL MOV')

        self.mov_x = True
        self.mov_y = False
        self.x = self.new_x
        self.y = self.new_y
        self.new_x = self.x + self.vel
        self.gastar_gas()

    def izquierda(self):
        if self.tanq_gaso < 0:
            raise NoHayGasolina()

        if self.veri_gas() <= 0:
            raise ValueError('EL GAS NO ES SUFICIENTE PARA REALIZAR EL MOV')

        self.mov_x = True
        self.mov_y = False
        self.y = self.new_y
        self.x = self.new_x
        self.new_x = self.x - self.vel
        self.gastar_gas()

    def arriba(self):
        if self.tanq_gaso <= 0:
            raise NoHayGasolina()

        if self.veri_gas() < 0:
            raise ValueError('EL GAS NO ES SUFICIENTE PARA REALIZAR EL MOV')

        self.mov_y = True
        self.mov_x = False
        self.y = self.new_y
        self.x = self.new_x
        self.new_y = self.y - self.vel
        self.gastar_gas()

    def abajo(self):
        if self.tanq_gaso <= 0:
            raise NoHayGasolina()

        if self.veri_gas() < 0:
            raise ValueError('EL GAS NO ES SUFICIENTE PARA REALIZAR EL MOV')

        self.mov_y = True
        self.mov_x = False
        self.y = self.new_y
        self.x = self.new_x
        self.new_y = self.y + self.vel
        self.gastar_gas()

    def __str__(self) -> str:
        return 'C'

    def __repr__(self) -> str:
        # return a green string
        return '\033[92m' + 'C' + '\033[0m'

