peso = float(input("Introduzca su Peso en Kilogramas: "))
altura = float(input("Introduzca su Altura en centometros: "))
altura_centimetros = altura / 100 
altura_2 = (altura_centimetros*altura_centimetros)
imc = peso / altura_2
print(f"Su IMC  es de = {imc:.2f}")

if imc < 18.5:
  print("Used esta en Bajo peso")
elif imc>=18.5 and  imc < 25:
  print("Su IMC es decuado")
elif imc>=25 and  imc < 30:
  print("Su IMC indica sobrepeso")
elif imc>=30 and  imc < 35:
  print("Su IMC indica Obesidad Grado I")
elif imc>=35 and  imc < 40:
  print("Su IMC indica Obesidad Grado II")
elif imc >= 40:
  print("Su IMC indica Obesidad Grado III")
else:
  print("vuelva a introducir los datos")