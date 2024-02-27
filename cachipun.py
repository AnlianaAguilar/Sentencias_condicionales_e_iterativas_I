import random

opciones = ["PIEDRA","PAPEL","TIJERA"]
computador = random.choice(opciones)
jugador = input("Que opicion eliges, PIEDRA, PAPEL o TIJERA?: ").upper()

if computador == "TIJERA" and jugador == "PIEDRA" or computador== "PIEDRA" and jugador == "PAPEL" or computador== "PAPEL" and jugador=="TIJERA":
  print(f"Tu jugaste {jugador}")
  print(f"El Computador jugo {computador}")
  print("Es un GANASTE!!!!!!")
elif computador == "PIEDRA" and jugador == "TIJERA" or computador == "PAPEL" and jugador == "PIEDRA" or computador == "TIJERA" and jugador== "PAPEL":
  print(f"Tu jugaste {jugador}")
  print(f"El Computador jugo {computador}")
  print("Es un Perdiste :(  ")
elif computador == jugador:
  print(f"Tu jugaste {jugador}")
  print(f"El Computador jugo {computador}")
  print("Es un empate")
else:
  print("Argumento inválido: Debe ser piedra, papel o tijera")