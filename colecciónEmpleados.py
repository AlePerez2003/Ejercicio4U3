import csv
import numpy as np
from numpy import ndarray
from claseEmpleado import Empleado
from claseContratado import Contratado
from clasePlanta import Planta
from claseExterno import Externo

class Coleccion:
    __cantidad: int
    __dimension: int
    __incremento: int
    __empleados: ndarray
    
    def __init__(self, dimension = 12, incremento = 10):
        self.__dimension = dimension
        self.__incremento = incremento
        self.__cantidad = 0
        
        
    def cargar_empleados(self):
        self.__empleados = np.empty(self.__dimension, dtype = Empleado)
        self.cargar_empleadosC()
        self.cargar_empleadosE()
        self.cargar_empleadosP()
    
    def cargar_empleadosC(self):
        cabecera = True
        with open('contratados.csv', 'r')as file:
            reader = csv.reader(file, delimiter = ';')
            for fila in reader:
                if cabecera:
                    cabecera = False
                else:
                    if self.__cantidad == self.__dimension:
                        self.__dimension += self.__incremento
                        self.__empleados.resize(self.__dimension)
                    else:
                        unEmpleado = Contratado(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], int(fila[6]), float(fila[7]))
                        self.__empleados[self.__cantidad] = unEmpleado
                        self.__cantidad += 1
            print('Empleados Contratados cargados con éxito')
                        
    def cargar_empleadosE(self):
        cabecera = True
        with open('externos.csv', 'r')as file:
            reader = csv.reader(file, delimiter = ';')
            for fila in reader:
                if cabecera:
                    cabecera = False
                else:
                    if self.__cantidad == self.__dimension:
                        self.__dimension += self.__incremento
                        self.__empleados.resize(self.__dimension)
                    else:
                        unEmpleado = Externo(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], float(fila[7]), float(fila[8]), float(fila[9]))
                        self.__empleados[self.__cantidad] = unEmpleado
                        self.__cantidad += 1
            print('Empleados Externo cargados con éxito')
                
    def cargar_empleadosP(self):
        cabecera = True
        with open('planta.csv', 'r')as file:
            reader = csv.reader(file, delimiter = ';')
            for fila in reader:
                if cabecera:
                    cabecera = False
                else:
                    if self.__cantidad == self.__dimension:
                        self.__dimension += self.__incremento
                        self.__empleados.resize(self.__dimension)
                    else:
                        unEmpleado = Planta(fila[0], fila[1], fila[2], fila[3], float(fila[4]), int(fila[5]))
                        self.__empleados[self.__cantidad] = unEmpleado
                        self.__cantidad += 1
            print('Empleados Planta cargados con éxito')
        
    def buscar_empleado(self, dni):
        i = 0
        bandera = False
        valor_retorno = -1
        while i < self.__cantidad and not bandera:
            if self.__empleados[i].get_dni() == dni:
                bandera = True
                valor_retorno = i
            else: 
                i += 1
        return valor_retorno
    
    def registrar_horas(self):
        horas = int(input('Ingrese las horas a registrar'))
        dni = input('Ingrese el dni del empleado')
        indice = self.buscar_empleado(dni)
        if indice == -1:
            print('El empleado no se encontro')
        else:
            if isinstance(self.__empleados[indice], Contratado):
                self.__empleados[indice].registrar_horas()
                print('Se registraron las horas exitosamente')
                
    def total_tarea(self):
        print('carpintería')
        print('electricidad')
        print('plomería')
        tarea = input('Ingrese una tarea')
        total = 0
        for i in range(self.__cantidad):
            if isinstance(self.__empleados[i], Externo):
                if self.__empleados[i].get_fecha_f() == 'Sin Finalizar':
                    total += self.__empleados[i].get_costo_obra()
        print('Para la tarea {} se debe pagar un total de ${}'.format(tarea, total))
        
    def ayuda_economica(self):
        for i in range(self.__cantidad):
            if self.__empleados[i].get_sueldo() < 150000:
                self.__empleados[i].listar_datos()
                print(self.__empleados[i].get_dni())
                
    def mostrar_sueldos(self):
        for i in range(self.__cantidad):
            self.__empleados[i].listar_datos()
            print('Sueldo: ${}'.format(self.__empleados[i].get_sueldo()))