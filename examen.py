import random
import csv

planilla=[]
with open ('examen.csv', 'r', newline='') as archivo_csv:
    reader=csv.reader(archivo_csv)
    for fila in reader:
        planilla.append(fila)

def asignar_sueldo():
    for empleado in planilla:
        empleado[2]=random.randint(300000, 2500000)

def clasificar_sueldos():
    total_sueldos_menores= 0
    total_sueldos_medianos=0
    total_sueldos_mayores=0
    sueldos_menores=[]
    sueldos_medianos=[]
    sueldos_mayores=[]
    for empleado in planilla:
        if empleado[2]<800000:
            total_sueldos_menores= total_sueldos_menores+1
            sueldos_menores.append(empleado)
    print("sueldos menores a $800000 TOTAL:", total_sueldos_menores, "\n nombre empleado | cargo | sueldo")
    for personas in sueldos_menores:
        print(personas)
    print("\n")
    
    for empleado in planilla:
        if empleado[2]>=800000 and empleado[2]<2000000:
            total_sueldos_medianos= total_sueldos_medianos+1
            sueldos_medianos.append(empleado)
    print("sueldos entre $800000 y $2000000 TOTAL:", total_sueldos_medianos, "\n nombre empleado | cargo | sueldo")
    for personas in sueldos_medianos:
        print(personas)
    print("\n")
    
    for empleado in planilla:
        if empleado[2]>2000000:
            total_sueldos_mayores= total_sueldos_mayores+1
            sueldos_mayores.append(empleado)
    print("sueldos mayores a 2000000 TOTAL:", total_sueldos_mayores, "\n nombre empleado | cargo | sueldo")
    for personas in sueldos_mayores:
        print(personas)
    print("\n")

def generar_reporte():
    print("nombre empleado | cargo | sueldo base | dcto salud | dcto afp | sueldo liquido")
    reporte=[]
    for empleado in planilla:
        nombre=empleado[0]
        cargo=empleado[1]
        sueldo_base=empleado[2]
        descuento_salud=sueldo_base*0.07
        descuento_afp=sueldo_base*0.12
        sueldo_liquido=sueldo_base-descuento_salud-descuento_afp
        reporte.append([nombre, cargo, sueldo_base, int(descuento_salud), int(descuento_afp), int(sueldo_liquido)])
    for persona in reporte:
        print(persona)
    print("\n")
    with open ('examen.csv', 'w', newline='')as archivo_csv:
        encabezado=['nombre empleado', 'cargo', 'sueldo base', 'dcto salud','dcto afp', 'sueldo liquido']
        reporte.insert(0, encabezado)
        writer=csv.writer(archivo_csv)
        writer.writerows(reporte)
while True:
    opcion=int(input("Seleccione una opcion:\n 1) Asignar sueldos aleatorios\n 2) Clasificar sueldos\n 3) Ver estadisticas\n 4) Generar reportes de sueldo\n 5) Salir\n"))
    if opcion==1:
        asignar_sueldo()
    if opcion==2:
        clasificar_sueldos()
    if opcion==3:
        print("no se xd")
    if opcion==4:
        generar_reporte()
    if opcion==5:
        print("Finalizando programa... \n Desarrollado por Catalina Rojas \n RUT: Me van a doxxear xd")
        break



    

