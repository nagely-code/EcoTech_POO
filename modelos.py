# clase padre

class Empleado:
    def __init__(self, id_empleado, nombre, correo, telefono, fecha_ingreso, sueldo):
       
        self.__id_empleado = id_empleado
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono
        self.__fecha_ingreso = fecha_ingreso
        self.__sueldo = sueldo
        self.__departamento = None   

    def Id(self):
        return self.__id_empleado

    def nombre(self):
        return self.__nombre

    def correo(self):
        return self.__correo

    def sueldo(self):
        return self.__sueldo

    def departamento(self):
        return self.__departamento

    # setters: para modificarlos, con validación
    def set_sueldo(self, nuevo_sueldo):
        if nuevo_sueldo < 0:
            print("El sueldo no puede ser negativo")
        else:
            self.__sueldo = nuevo_sueldo

    def set_departamento(self, departamento):
        self.__departamento = departamento

    def mostrar_informacion(self):
        print("Empleado ID:", self.__id_empleado, " - Nombre:", self.__nombre, " - Correo:", self.__correo)


# Hija

class Administrador(Empleado):
    def __init__(self, id_empleado, nombre, correo, telefono, fecha_ingreso, sueldo, id_administrador, contraseña):
        super().__init__(id_empleado, nombre, correo, telefono, fecha_ingreso, sueldo)
        self.__id_administrador = id_administrador
        self.__contraseña = contraseña

    def validar_contraseña(self, intento):
        return intento == self.__contraseña

    def registrar_empleado(self, empleado):
        print("Administrador", self.nombre(), " se ha registrado", empleado.nombre())

    def generar_informe(self):
        print("Informe Administrador ID:", self.__id_administrador)


class Departamento:
    def __init__(self, id_departamento, nombre, correo, gerente_asociado):
        self.__id_departamento = id_departamento
        self.__nombre = nombre
        self.__correo = correo
        self.__gerente_asociado = gerente_asociado
        self.__empleados = []

    def nombre(self):
        return self.__nombre

    def asignar_empleado(self, empleado):
        self.__empleados.append(empleado)
        empleado.set_departamento(self)   # el empleado también sabe su departamento
        print("Empleado", empleado.nombre(), "asignado al departamento", self.__nombre)


class Proyecto:
    def __init__(self, id_proyecto, nombre, descripcion, fecha_inicio):
        self.__id_proyecto = id_proyecto
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__fecha_inicio = fecha_inicio
        self.__empleados = []

    def nombre(self):
        return self.__nombre

    def asignar_empleado(self, empleado):
        self.__empleados.append(empleado)

    def crear_proyecto(self):
        print("Proyecto,", self.__nombre, " creado con exito.")

    def modificar_proyecto(self, nuevo_nombre, nueva_desc):
        self.__nombre = nuevo_nombre
        self.__descripcion = nueva_desc

    def borrar_proyecto(self):
        print("Proyecto ID", self.__id_proyecto, "eliminado")


class RegistroTiempo:
    def __init__(self, id_registro, horas_trab, descripcion, fecha_inicio, empleado, proyecto):
        self.__id_registro = id_registro
        self.__horas_trab = horas_trab
        self.__descripcion = descripcion
        self.__fecha_inicio = fecha_inicio
        self.__empleado = empleado
        self.__proyecto = proyecto

    def horas_trab(self):
        return self.__horas_trab