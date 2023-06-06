from claseEmpleado import Empleado

class Contratado(Empleado):
    __fecha_inicio: str
    __fecha_finalizacion: str
    __horas_trabajadas: int
    __valor_hora: float
    
    def __init__(self, dni, nombre, direccion, telefono, fecha_i, fecha_f, horas, valor_h):
        super().__init__(dni, nombre, direccion, telefono)
        self.__fecha_inicio = fecha_i
        self.__fecha_finalizacion = fecha_f
        self.__horas_trabajadas = horas
        self.__valor_hora = valor_h
    
    def get_sueldo(self):
        sueldo = self.__horas_trabajadas * self.__valor_hora
        return sueldo
    
    def registrar_horas(self, horas):
        self.__horas_trabajadas += horas