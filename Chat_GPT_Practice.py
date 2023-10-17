#Crea un programa en Python que permita llevar un registro de estudiantes y sus calificaciones en diferentes asignaturas. 
import statistics
registro_estudiantes={}

welcome= input(str("¿Quieres añadir un alumno? "))
if welcome == "si":
    while True:
        print("1. Agregar lista de estudiantes")
        print("2. Mostrar la lista de estudiantes")
        print("3. Mostrar las calificaciones del estudiante")
        print("4. Calcular promedio de calificaciones de un estudiante")
        print("5. Calcular el promedio de todas las asignaturas")
        print("6. Salir")

        opcion= input(str("selecciona una opción: "))

        if opcion == "1":
            nuevo_alumno= (input(str("Escriba el nombre del alumno: ")))
            calificaciones = {
                "Mates": int(input("Inserte nota de Matemáticas: ")),
                "Lengua": int(input("Inserte nota de Lengua: ")),
                "Física": int(input("Inserte nota de Física: ")),
                "Música": int(input("Inserte nota de Música: ")),
                "Inglés": int(input("Inserte nota de Inglés: "))
            }

            registro_estudiantes[nuevo_alumno] = calificaciones
          
            print("El alumno"+ nuevo_alumno +" se ha incrito correctamente")
        elif opcion=="2":
            print("\nLista de estudiantes:")
            for estudiante in registro_estudiantes:
                print(estudiante)
        elif opcion=="3":
            nombre = input("Inserte el nombre del estudiante: ")
            if nombre in registro_estudiantes:
                print("Calificaciones de " + nombre + ":")
                for asignatura, nota in registro_estudiantes[nombre].items():
                    print(asignatura + ": " + str(nota))
        elif opcion=="4":
            if nombre in registro_estudiantes:
                calificaciones = list(registro_estudiantes[nombre].values())
                promedio = statistics.mean(calificaciones)
                print("El promedio de calificaciones de " + nombre + " es: " + str(promedio))
            else:
                 print("Estudiante no encontrado en el registro.")
        elif opcion=="5":
             # Calcular el promedio de todas las asignaturas
            promedios_asignaturas = {}
            for asignatura in registro_estudiantes[nombre].keys():
                notas_asignatura = [registro_estudiantes[estudiante][asignatura] for estudiante in registro_estudiantes]
                promedio_asignatura = statistics.mean(notas_asignatura)
                promedios_asignaturas[asignatura] = promedio_asignatura

            print("Promedio de todas las asignaturas:")
            for asignatura, promedio in promedios_asignaturas.items():
                print(asignatura + ": " + str(promedio))

        elif opcion =="6":
            print("Saliendo del programa...")
            break 
           

else:
    print("Hasta luego")  
   
