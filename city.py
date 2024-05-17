from car_for_city import (
    Car,
    ColorClass,
    MarcasClass
    )

# TODO: Crea un mapa en forma de matrix de 50x50

# en la matriz se van a representar las calles y los edificios
# las calles, van a ser representadas por 0
# y los edificios por 1

# auto_1.initializar_posicion(0, 0)

# Agregamos 4 metodos
# - adelante
# - atras
# - derecha
# - izquierda

# Si el carro tiene velocidad 1,
# este se mueve 1 espacio, si tiene velocidad 2, se mueve 2 espacios
# Es decir new_pos = pos.eje_elegido + vel


# si new_pos == 1, print('Yo soy un tesla, no puedo atravesar edificios')

# Punto A y el punto B hay un kilometro de diferencia
# Punto A y el punto B hay un metro de diferencia -> 1000 veces

class InitCarError(Exception):
    def __init__(self, *args: object) -> None:
        self.mensaje = "EL CARRO NO PUEDE INICIALIZAR EN ESTA POSICION"
        super().__init__(self.mensaje)


class LimitMapError(Exception):
    def __init__(self, *args) -> None:
        self.mensaje: str = "ESTAS SUPERANDO EL LIMITE DEL MAPA "
        super().__init__(self.mensaje)


class CityMap():
    def __init__(self, car: Car) -> None:
        self.road: int = 0
        self.edifcio: int = 1
        self._base: list[list[list]] = []
        self.car: Car = car
        self.size_map: int = 20
        self._init_x: int = 0
        self._init_y: int = 0
        self.init: bool = False

    def create_base(self):

        for _ in range(self.size_map):  # Esto pasa X veces
            lista = []
            for _ in range(self.size_map):  # Esto pasa X veces
                lista.append(self.road)
            self._base.append(lista)

    def create_base_2(self):
        i: int = 1
        i2: int = 0
        a: bool = True
        for _ in range(self.size_map):
            lista: list[int | Car] = []
            for _ in range(self.size_map):
                if a:
                    n = self.road
                    if i == 4:
                        i = 0
                    if i >= 2:
                        n = self.edifcio
                    lista.append(n)
                    i += 1
                    continue
                lista.append(self.road)
            self._base.append(lista)
            i2 += 1
            i = 1
            if i2 == 2:
                a = not a

                i2 = 0

    def init_car(self, y: int, x: int):
        # posiblemente tenga que hacer que los valores nx y ny del carro sean
        # igual a los valores de inicializacion
        self._init_x = x
        self._init_y = y
        self.car.new_y = y
        self.car.new_x = x
        if (
            self._base[self._init_y][self._init_x] == 1 or
            self._base[self._init_y][self._init_x] == Car
                ):
            raise InitCarError()
        self._base[self._init_y][self._init_x] = self.car
        self.init = True

    def is_space_empty(self, x: int, y: int) -> bool:

        if self._base[y][x] == 1 or self._base[y][x] == Car:
            return False
        return True

    def ver_y(self) -> int:
        old_y: int = self.car.y
        new_y: int = self.car.new_y
        old_x: int = self.car.x
        count_p: int = 0

        for p in range(old_y, new_y+1):
            count_p += 1
            if self.is_space_empty(old_x, p):
                return new_y - count_p
        return new_y

    def ver_x(self) -> int:
        old_x: int = self.car.x
        new_x: int = self.car.new_x
        old_y: int = self.car.y
        count_e: int = 0

        for e in range(old_x, new_x+1):
            if self.is_space_empty(e, old_y):
                return old_x + count_e
            count_e += 1
        return new_x

    def validate_mov(self) -> int:
        pass

    def update_map(self):
        x: int = self.car.x
        y: int = self.car.y
        n_x: int = self.ver_x()
        n_y: int = self.ver_y()

        if n_x >= self.size_map or n_y >= self.size_map:
            raise LimitMapError()

        if self.init and self._base[self._init_y][self._init_x] != Car:
            self._base[self._init_y][self._init_x] = 0
            self.init = False

        self._base[y][x] = 0
        self._base[n_y][n_x] = self.car

    def __str__(self) -> str:

        for i in self._base:
            print(i)
        return ''


supra = Car(
            color=ColorClass.NEGRO.name,
            marca=MarcasClass.TOYOTA.name,
            modelo="supra",
            wheels_info=[
                {
                    'MARCA': MarcasClass.TOYOTA,
                    'COLOR': ColorClass.AZUL
                }
                ],
            doors_info=[
                {
                    'COLOR': ColorClass.AZUL
                }
            ],
            tanq_gaso_max=100
        )

city = CityMap(supra)

city.create_base_2()

city.init_car(0, 0)

# Car
supra.create_engine()
supra.create_doors()
supra.start()

for i in range(6):
    supra.acelerar(1)
    supra.derecha()
    city.update_map()
    print(f'vieja pos en x: {supra.x}')
    print(f'vieja pos en y: {supra.y}')
    print(f'pos en x: {supra.new_x}')
    print(f'pos en y: {supra.new_y}')
    print(city)

# ---------------

# print(f'antigua posicion: {supra.y}')
# print(f'nueva posicion: {supra.new_y}')


# # city.update_map()

# print(supra.vel)
# print(city)
# supra.abajo()
# city.update_map()

# print(f'antigua posicion: {supra.y}')
# print(f'nueva posicion: {supra.new_y}')
# print(city)

# supra.derecha()
# city.update_map()
# print(city)

# for i in range(16):
#     supra.abajo()
#     city.update_map()

# print(city)
# ((0,1,1,0,1,1,0),
#  (0,1,1,0,1,1,0)
#  (0,0,0,0,0,0,0),
#  (0,0,0,0,0,0,0)
#  (0,1,1,0,1,1,0),
#  (0,1,1,0,1,1,0)
#  (0,0,0,0,0,0,0),
#  (0,0,0,0,0,0,0),
#  (0,1,1,0,1,1,0),
#  (0,1,1,0,1,1,0)
# )
