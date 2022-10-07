edificio={
   "Marketing": [],
   "Recursos humanos": [],
   "Contabilidad": [],
   "Ventas": [],
}

while True:
    print("PLATAFORMA ADMINISTRATIVA DEL EDIFICIO")
    print("""
    1. Ingreso al edificio
    2. Salida del edificio
    3. Estadísticas
    4. Salir
    """)
    print()
    
    a = input("Ingrese la acción que quiere realizar: ")

    while a != "1" and a != "2" and a != "3" and a != "4":
        a = input("Ingreso invalido. Intente otra vez: ")
    
    print()

    if a == "1":
        print("INGRESO AL EDIFICIO\n")

        # se solicita info de la persona
        first_name = input("Nombre: ")
        while not first_name.isalpha():
            first_name = input("Ingreso inválido. Intente nuevamente: ")
        last_name = input("Apellido: ")
        while not last_name.isalpha():
            last_name = input("Ingreso inválido. Intente nuevamente: ")
        
        # para validar la cédula hay un par de pasos extra. hay que ver si ya está guardada. en caso de que sí, debe solicitarse otra vez
        dni = input("Cédula: ")

        # variable auxiliar unique para ver si existe o no
        unique = True
        # loop para revisar cada cédula para ver si es igual al input o no
        for dept in edificio:
            for person in edificio[dept]:
                if person["Cédula"] == dni:
                    unique = False
                    break
            if not unique:
                break

        while not dni.isnumeric() or not unique:
            dni = input("Ingreso inválido. Intente nuevamente: ")
            unique = True
            for dept in edificio:
                for person in edificio[dept]:
                    if person["Cédula"] == dni:
                        unique = False
                        break
                if not unique:
                    break

        age = input("Edad: ")
        while not age.isnumeric() or int(age) == 0:
            age = input("Ingreso inválido. Intente nuevamente: ")

        print()
        # se muestran los departamentos numerados. el enumerate para diccionarios me trae el índice y el key de cada cosa
        for i, dept in enumerate(edificio):
            print(i+1, dept) # +1 porque i comienza en 0 y yo quiero que se vea desde 1

        # pregunto el número correspondiente al departamento
        dept_idx = input("\nIngrese el número correspondiente al departamento al que pertenece: ")

        # valido que me hayan dado un número y que ese número sea alguno de los índices. si tengo 4 departamentos, puedo tener 0, 1, 2 o 3 como índice
        while not dept_idx.isnumeric() or int(dept_idx)-1 not in range(len(edificio)):
            dept_idx = input("Ingreso inválido. Ingrese el número correspondiente al departamento al que pertenece: ")
        
        # uso el índice ingresado por teclado (que ya se que existe) y consigo el nombre del departamento correspondiente a ese índice. .keys() es un método de diccionarios que me trae una especie de lista con todos los keys (en este caso todos los nombres de los departamentos)
        # eso lo hago para guardar en la lista correspondiente al departamento la info de la persona en forma de diccionario
        edificio[list(edificio.keys())[int(dept_idx) - 1]].append({ "Nombre": first_name, "Apellido": last_name, "Cédula": dni, "Edad": int(age)})

        print("¡Persona registrada exitosamente!")

        print("\nPERSONAS EN EL EDIFICIO ACTUALMENTE\n") # esto no se evaluó. lo estoy poniendo porque quiero
        for dept, ppl in edificio.items(): # para cada dept (str) con su respectiva lista de personas dentro del edificio (diccionario)
            print(f"* DEPARTAMENTO DE {dept.upper()}")
            for person in ppl: # para cada persona (diccionario) dentro de la lista de personas
                print(f"\t- Nombre: {person['Nombre']}\n\t- Apellido: {person['Apellido']}\n\t- Cédula: {person['Cédula']}\n\t- Edad: {person['Edad']}\n")

        
    
    elif a == "2":
        print("SALIDA DEL EDIFICIO\n")

        # se muestra la lista de personas del edificio
        for dept, ppl in edificio.items(): # para cada dept (str) con su respectiva lista de personas dentro del edificio (diccionario)
            print(f"* DEPARTAMENTO DE {dept.upper()}")
            for person in ppl: # para cada persona (diccionario) dentro de la lista de personas
                print(f"\t- Nombre: {person['Nombre']}\n\t- Apellido: {person['Apellido']}\n\t- Cédula: {person['Cédula']}\n\t- Edad: {person['Edad']}\n")

        print()
        delete_dni = input("Ingrese el número de cédula de la persona que desea eliminar: ")

        found = False # esto es para avisar si la persona existe o no

        # busco a la persona por cédula
        for dept in edificio:
            for i, person in enumerate(edificio[dept]):
                if person["Cédula"] == delete_dni:
                    found = True
                    edificio[dept].pop(i) # el .pop() recibe el índice de lo que se quiera borrar como parámetro

                    print("\nSe ha eliminado exitosamente a la siguiente persona del edificio:")
                    print(f"\t- Nombre: {person['Nombre']}\n\t- Apellido: {person['Apellido']}\n\t- Cédula: {person['Cédula']}\n\t- Edad: {person['Edad']}\n")

                    break
            if found:
                break

        if not found:
            print(f"\nNo hay personas en el edificio con cédula {delete_dni}")

        print("\nPERSONAS EN EL EDIFICIO ACTUALMENTE\n") # esto no se evaluó. lo estoy poniendo porque quiero
        for dept, ppl in edificio.items(): # para cada dept (str) con su respectiva lista de personas dentro del edificio (diccionario)
            print(f"* DEPARTAMENTO DE {dept.upper()}")
            for person in ppl: # para cada persona (diccionario) dentro de la lista de personas
                print(f"\t- Nombre: {person['Nombre']}\n\t- Apellido: {person['Apellido']}\n\t- Cédula: {person['Cédula']}\n\t- Edad: {person['Edad']}")



    elif a == "3":
        print("ESTADÍSTICAS\n")

        total_ppl = 0 # para ir acumulando la cantidad de gente por depa. al final da la cantidad de gente total
        total_ages_sum = 0 # para ir acumulando las edadess de todas las personas del edificio. con esto se calcula el promedio del total

        print("--- CANTIDAD DE PERSONAS POR DEPARTAMENTO ---")
        for dept in edificio:
            total_ppl += len(edificio[dept])
            print(f"- {dept}: {len(edificio[dept])}")

        print()
        print("--- CANTIDAD TOTAL DE PERSONAS EN EL EDIFICIO ---")
        print(total_ppl, '\n')

        print("--- PROMEDIO DE EDAD POR DEPARTAMENTO ---")
        for dept in edificio:
            sum_of_ages = 0 # variable auxiliar donde voy acumulando las edades de las personas del departamento actual (dept)
            for persona in edificio[dept]:
                sum_of_ages += persona["Edad"]
            
            total_ages_sum += sum_of_ages # agrego la suma de edades al acumulador de las edades de todo el edificio
            
            if len(edificio[dept]) > 0: # si hay por lo menos una persona en el depa, se saca el promedio (si no se pone esto puede dar un error de división entre cero)
                print(f"- {dept}: {sum_of_ages / len(edificio[dept])}")
            else:
                print(f"- {dept}: -")

        print()
        print("--- PROMEDIO DE EDAD EN EL EDIFICIO ---")
        if total_ppl > 0:
            print(total_ages_sum / total_ppl, '\n')
        else:
            print("-")


    else:
        break

    print("\n\n--------------------------------------")