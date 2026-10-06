nombre = str(input("¿Cuál es su nombre?"))
edad = int(input("¿Cuál es su edad?"))
nota1 =float( input("Ingrese su primera nota"))
nota2 = float(input("Ingrese su segunda nota"))
nota3 =  float(input("Ingrse su tercer nota"))
promedio = (nota1 + nota2 + nota3)/3
if promedio>71:
    print("Aprobado")
else :
    print("Reprobado")

