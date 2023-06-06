class Empleado:
    __dni: str
    __nombre: str
    __direccion: str 
    __telefono: str
    
    def __init__(self, dni, nombre, direccion, telefono):
        self.__dni = dni
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        
    def get_sueldo(self):
        pass
    
    def get_dni(self):
        return self.__dni
    
    def listar_datos(self):
        print('----------------')
        print(self.__nombre)
        print(self.__direccion)

    
    