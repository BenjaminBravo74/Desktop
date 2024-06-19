horas= float(input("ingrese las horas trabajadas: "))
valorhora=float(input("ingrese el valor de la hora: "))
sueldo= horas*valorhora
if valorhora <= 40:
    print("su sueldo es de ",sueldo)
else:
    horaextra= float(input("ingrese el numero de horas extras que realizo: "))
    valorhoraextra= valorhora* 1.50
    sueldofinal= sueldo + valorhoraextra
    print("su sueldo es de ",sueldofinal)