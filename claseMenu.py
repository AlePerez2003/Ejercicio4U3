from colecciónEmpleados import Coleccion

class Menu:
    __cod: int
    
    def mostrar_opciones(self):
        print('Opcion 1: cargar empleados')
        print('Opcion 2: registrar horas de un empleado')
        print('Opcion 3: mostrar monto total a pagar por una tarea')
        print('Opcion 4: mostrar empleados que necesitan ayuda económica')
        print('Opcion 5: mostrar el sueldo de todos los empleados de la empresa')
        print('Opcion 0: finalizar operacion')
        
    def ejecutar_menu(self, CE:Coleccion):
        self.mostrar_opciones()
        self.__cod = int(input('Ingrese el codigo'))
        while self.__cod != 0:
            if self.__cod == 1:
                CE.cargar_empleados()
            elif self.__cod == 2:
                CE.registrar_horas()
            elif self.__cod == 3:
                CE.total_tarea()
            elif self.__cod == 4:
                CE.ayuda_economica()
            elif self.__cod == 5:
                CE.mostrar_sueldos()
            else:
                print('Codigo incorrecto')
            self.mostrar_opciones()
            self.__cod = int(input('Ingrese el codigo'))