from claseEmpleado import Empleado

class Externo(Empleado):
    __tarea: str
    __fecha_inicio: str
    __fecha_finalizacion: str
    __viatico: float
    __costo_obra: float
    __seguro_vida: float
    
    def __init__(self, dni, nombre, direccion, telefono, tarea, fecha_i, fecha_f, viatico, costo, seguro):
        super().__init__(dni, nombre, direccion, telefono)
        self.__tarea = tarea
        self.__fecha_inicio = fecha_i
        self.__fecha_finalizacion = fecha_f
        self.__viatico = viatico
        self.__costo_obra = costo
        self.__seguro_vida = seguro
        
    def get_sueldo(self):
        sueldo = self.__costo_obra - self.__viatico - self.__seguro_vida
        return sueldo
    
    def get_fecha_f(self):
        return self.__fecha_finalizacion
    
    def get_costo_obra(self):
        return self.__costo_obra