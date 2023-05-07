from manejador_alumnos import ManejadorAlumnos
from manejador_materias import ManejadorMaterias

# Cargar datos de los archivos
manejador_alumnos = ManejadorAlumnos()
manejador_alumnos.cargar_alumnos('alumnos.csv')

manejador_materias = ManejadorMaterias()
manejador_materias.cargar_materias('materiasAprobadas.csv')

# Menú de opciones
while True:
    print("\n=== MENÚ ===")
    print("1. Calcular promedio de un alumno")
    print("2. Estudiantes que aprobaron una materia en forma promocional")
    print("3. Listado de alumnos ordenado")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        dni = int(input("Ingrese el número de DNI del alumno: "))
        promedio_con_aplazos, promedio_sin_aplazos = manejador_alumnos.calcular_promedio(dni, manejador_materias)
        if promedio_con_aplazos is not None:
            print(f"Promedio con aplazos del alumno con DNI {dni}: {promedio_con_aplazos:.2f}")
            print(f"Promedio sin aplazos del alumno con DNI {dni}: {promedio_sin_aplazos:.2f}")
        else:
            print("No se encontró ningún alumno con ese DNI")

    elif opcion == '2':
        nombre_materia = input("Ingrese el nombre de la materia: ")
        estudiantes_aprobados = manejador_materias.estudiantes_aprobados_promocion(nombre_materia)
        if len(estudiantes_aprobados) > 0:
            print("Estudiantes que aprobaron la materia en forma promocional:")
            print("DNI\tApellido y nombre\tFecha\t\tNota\tAño que cursa")
            for estudiante in estudiantes_aprobados:
                print(f"{estudiante.dni}\t{estudiante.apellido} {estudiante.nombre}\t{estudiante.fecha}\t{estudiante.nota}\t{manejador_alumnos.alumnos[estudiante.dni-1].anio}")
        else:
            print("No se encontraron estudiantes que aprobaron la materia en forma promocional")

    elif opcion == '3':
        alumnos_ordenados = sorted(manejador_alumnos.alumnos)
        if len(alumnos_ordenados) > 0:
            print("Listado de alumnos ordenado:")
            print("DNI\tApellido y nombre\tCarrera\tAño que cursa")
            for alumno in alumnos_ordenados:
                print(f"{alumno.dni}\t{alumno.apellido} {alumno.nombre}\t{alumno.carrera}\t{alumno.anio}")
        else:
            print("No se encontraron alumnos")

    elif opcion == '4':
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
