from os import system

#Clase Pacientes
class Pacientes:
    def __init__(self, nombre, apellido, pasaporte, fechaDeNacimiento, edad, paisDeResidencia, genero, estatus):
        self.nombre = nombre
        self.apellido = apellido
        self.fechaDeNacimiento = fechaDeNacimiento
        self.edad = edad
        self.paisDeResidencia = paisDeResidencia
        self.genero = genero
        self.estatus = estatus
        self.pasaporte = pasaporte
        
	#Meodo para registrar a los pacientes
    def registrarPacientes(self):
        print('Registrar a Personas Con Posible Caso de covid-19')
        pacienteticos = open('RegistroPacientes.txt', 'a'
'')
        pacienteticos.write(f'''Nombre: {self.nombre}
Apellido: {self.apellido}
FechaDeNacimiento: {self.fechaDeNacimiento}
Edad: {self.edad}
Genero: {self.genero}
Estatus: {self.estatus}
Pasaporte: {self.pasaporte}
''')
        pacienteticos.close()
        
	#Metodo para mostrar Pacientes Registrados
    def mostrarPacientesConPosiblesCasos(self):
        print(f'''¡PERSONAS REGISTRADAS!
nombre:{nombre}
Apellido:{apellido}
Fecha de nacimiento:{fechaDeNacimiento}
Edad: {edad}
Pais de residencia: {paisDeResidencia}
Genero: {genero}
Estatus: {estatus}
Pasaporte:{pasaporte}''')

#Metodo para validar los Espacios vacios
def Validaciones(revisar):
	while revisar == '':
		revisar = input('¡No Puedes Dejar Espacios vacios!\n Rellene la Pregunta: : ')
	return revisar

#Main del Programa / Menú
exit = False
while exit == False:

    print("		*********************************")
    print("		*  ¡BIENVENIDO A LOS CHEQUEOS!  *")
    print("		*       por coronavirus         *")
    print("		*                               *")
    print("		*      REGISTRO DE CASOS        *")
    print("		*          CORONAVIRUS          *")
    print('		*********************************')
    print('		---------------------------------')
    print('')
    print('''		BIENVENIDO QUE DESEA REALIZAR   
     ------Ingrese una Opcion------
    1- Registrar Pacientes Con Posibles Casos de COVID-19
    2- Casos Encontrados por: pais, genero y edad
    3- Modicar Estatu del Paciente Registrado: activos / inactivos
    4- Casos activos: Recuperados / Fallecidos
    5- Visualizar los DATOS de las persona de mayor y menor edad
    6- Salir
    ''')

    opc = input()
    opc = Validaciones(opc)
    system('cls')
    if opc == '1':
		
        print('---INGRESO AL REGISTRO DE PACIENTES---')
        print('--------------------------------------')
        print('Ingrese los datos de la persona con posible caso de coronavirus')
        nombre = input('Digite el nombre del Paciente: ')
        nombre = Validaciones(nombre)
        apellido = input('Digite el apellido  : ')
        apellido = Validaciones(apellido)
        pasaporte = input('Ingrese el Pasaporte  : ')
        pasaporte = Validaciones(pasaporte)
        fechaDeNacimiento = input('Digite la Fecha de Nacimiento  : ')
        fechaDeNacimiento = Validaciones(fechaDeNacimiento)
        paisDeResidencia = input('Pais De Origen: ')
        paisDeResidencia = Validaciones(paisDeResidencia)
        edad = input('Ingrese la Edad del Paciente: ')
        edad = Validaciones(edad)
        estatus = 'Sospechoso'
        print('''Selecciones el genero del paciente
        1.- Hombre
        2.- Mujer''')
        opc2 = input()
        system('cls')
        if opc2 == '1':
            genero ='Hombre'
        elif opc2 == '2':
            genero ='Mujer'
        else: 
            print("Opcion invalida")
            input()
            opc2 = Validaciones(opc2)
   
        NuevoPaciente = Pacientes(nombre, apellido, pasaporte, fechaDeNacimiento, edad, paisDeResidencia, genero, estatus)
        NuevoPaciente.registrarPacientes()
        NuevoPaciente.mostrarPacientesConPosiblesCasos()
        system('cls')

    if opc == '2':
	
        print('---HA INGRESO A LOS COSAS REGISTRADOS POR:\n1.-País\n2.-Genero\n3.-edad\n')
        opc3 = input()
        system('cls')
        pacienteticos = open('RegistroPacientes.txt', 'r')
        reditt = pacienteticos.readlines()
        pacienteticos.close()
        if opc3 == '1':
            pais= input('Digiti El Nombre Del País')
            pais= Validaciones(pais)
            boolPais = reditt.count('Pais: '+{pais}+'\n')
            print(f'El Numero de Personas con Casos de Sospechas son: {boolPais}')
        if opcion1 == '2':
            acount = reditt.count('Genero: '+'Femenino'+'\n')
            print(f'Casos en las mujeres: {acount}')
            hombres = reditt.count('Genero: '+'Masculino'+'\n')
            print(f'Casos en los hombres: {hombres}')
        if opcion1 == '3':
            EdadPersonas = input('Ingrese la edad: ')
            EdadPersonas = Validaciones(EdadPersonas)
            boolEdad = reditt.count('Edad: '+EdadPersonas+'\n')
            print(f'Los casos de sospechosos por edad son: {boolEdad}')
        else:
		
            print('Opcion Invalida')  
            system('cls') 
    if opc == '3':
        print("-----------------------------------")
        pacienteticos = open('RegistroPacientes.txt', 'r')
        reditt = pacienteticos.readlines()
        pacienteticos.close()
        PasaporteIngresado = input('Ingrese el pasaporte de la persona con posible caso')
        if 'cedula: '+PasaporteIngresado+'\n' in reditt:
            print('''!Ingrese los Sintomas Que Presenta el PACIENTE!
            1.- Secreciones Nasales, Dolor De Garganta, Tos Seca, Dificultad Para Respirar
            2.- Tos Con Flema, Congestion Nasal / Estornudos, Dolor DE Cabeza, Escalofrios, Perdida de Olfato
            3.- Picor Nasal, Estornudos, Fiebre, Salpullido''')
            opc4 = input()
            opc4 = Validaciones(opc4)
            system('cls')
            if opc4 == '1':
                print('Este Paciente Posee COVID-19-"CORONAVIRUS"- ')
                for pacienteC19 in reditt:
                    pacienteC19 = reditt.replace('Estatus: '+'Sospechoso'+'\n', 'Estatus: '+'Confirmado'+'\n')
                    reditt.append(pacienteC19)
                estatus = 'CONFIRMADO'
            elif opc4 == '2':
                print('El Paciente Presente un Resfriado Común')
                estatus = 'DEESCARTADO'
            elif opc4 == '3':
                print('El Paciente Presenta Una Alergia')
                estatus = 'DESCARTADO'
            else:
                print('Opcion Invalida')
        else:
            print('No Existen Datos De Este Paciente')
            system('cls')
	
    if opc == '4':

        boolRecuperados = reditt.count('Estatus: '+'Recuperado'+'\n')
        print(f'Personas Resuperadas: {boolRecuperados}')
        boolFallecidos = reditt.count('Estatus: '+'Fallecido'+'\n')
        print(f'Personas Fallecidas: {boolFallecidos}')
        system('cls')
    if opc == '5':
	
        print('---Ha Ingresado a DATOS de los Pacientes:\n1.-Mayor de Edad\n2.-Menor de Edad\n')
        opcs = input()
        opcs= Validaciones(opcs)
        system('cls')
        pacienteticos = open('RegistroPacientes.txt', 'r')
        reditt = pacienteticos.readlines()
        pacienteticos.close()
        if opcs == '1':
            edad= input('Digite la Edad')
            edad = Validaciones(edad)
            if edad<18:
                boolEdades = reditt.count('Menor: '+{edad<18}+'\n')
                print(f'El numero de Pacientes Menores de Edad son: {boolEdades}')
            else:
                print ("")
        elif opcs =='2':
            edad= input('Digite la Edad')
            edad= Validaciones(edad)
            if edad>=18:
                boolEdades = reditt.count('Mayor: '+{edad>18}+'\n')
                print(f'El numero de Pacientes Menores de Edad son: {boolEdades}')
                system('cls')
            else:
                print('Error-')
        else:

            print('Opcion Invalida')
            system('cls')
    if opc == '6':
        salida = True
