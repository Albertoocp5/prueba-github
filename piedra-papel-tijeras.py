import random

opciones = ["Piedra", "Papel", "Tijeras"]

print("¡Juguemos a Piedra, Papel, Tijeras!")
jugador = input("Elige una de las tres: ").lower()
pc = random.choice(opciones)

print(f"Tu elegiste: {jugador}")
print(f"El PC elgió: {pc}")

if jugador==pc:
  print "Hemos quedado empate! Juguemos otra."
  jugador = input("Elige una de las tres: ").lower()
  pc = random.choice(opciones)
elif (jugador == "piedra" and pc == "tijera") or \
     (jugador == "papel" and pc == "piedra") or \
     (jugador == "tijera" and pc == "papel"):
    print("¡Ganaste!")
elif jugador in opciones:
    print("¡Perdiste!")
else:
    print("Opción inválida, intenta con piedra, papel o tijera.")
