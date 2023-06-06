from claseEmpleado import Empleado

class Planta(Empleado):
    __sueldo: float
    __antigüedad: int
    
    def __init__(self, dni, nombre, direccion, telefono, sueldo, antiguedad):
        super().__init__(dni, nombre, direccion, telefono)
        self.__sueldo = sueldo
        self.__antigüedad = antiguedad
    
    def get_sueldo(self):
        sueldo = self.__sueldo + ((self.__sueldo / 100) * self.__antigüedad)
        return sueldo