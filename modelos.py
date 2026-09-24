# clase padre

class Empleado:
    def __init__(self,id_empleado, nombre, correo, telefono, fecha_ingreso, sueldo):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.corre = correo
        self.telefono = telefono
        self.fecha_ingreso = fecha_ingreso
        self.sueldo = sueldo

    def Id(self):
        return self.id_empleado

    def nombre(self):
        return self.nombre

    def mostrar_informacion(self):
        print("Empleado ID:", self.id_empleado, " - Nombre:", self.nombre, " - Correo:", self.correo)



# Hija

class Administrador(Empleado):
    def __init__(self, id_empleado, nombre, correo, telefono, fecha_ingreso, sueldo, id_administrador, contraseña):

        super().__init__(id_empleado, nombre, correo, telefono, fecha_ingreso, sueldo)
        self.id_administrador = id_administrador
        self.contraseña = contraseña


    def registrar_empleado(self, empleado):
        print("Administrador", self.nombre, " se ha registrado", empleado.nombre())

    def generar_informe(self):
        print("Informe Administrador ID:", self.id_administrador)


class Departamento:
    def __init__(self, id_departamento, nombre, correo, gerente_asociado):
        self.id_departamento = id_departamento
        self.nombre = nombre
        self.correo = correo
        self.gerente_asociado = gerente_asociado
        self.empleado = []

    def asignar_empleado(self, empleado):
        self.empleado.append(empleado)
        print("Empleado", empleado.nombre(), "asignado al departamento", self.nombre)

class Proyecto:
    def __init__(self, id_proyecto, nombre, descripcion, fecha_inicio):
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.empleados = []

    def crear_proyecto(self):
        print("Proyeto,", self.nombre, " creado con exito.")

    def modificar_proyecto(self, nuevo_nombre, nueva_desc):
        self.nombre = nuevo_nombre
        self.descripcion = nueva_desc

    def borrar_proyecto(self):
        print("Proyecto ID", self.id_proyecto, "eliminado")


class registroTiempo:
    def __init__(self, id_registro, horas_trab, descripcion, fecha_inicio, empleado, proyecto):
        self.id_registro = id_registro
        self.horas_trab = horas_trab
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.empleado = empleado
        self. proyecto = proyecto

        

