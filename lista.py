
print("Bienvenido al registro de invitados.")
print("Debes ingresar la cantidad exacta de nombres que indiques.\n")

cantidad_nombres = int(input("¿Cuántos nombres deseas ingresar?: "))

invitados = []

for i in range(cantidad_nombres):
    nombre = input(f"Escribe un nombre: ").strip()  
    invitados.append(nombre.upper())  

print("\nLista de invitados:")
for invitado in invitados:
    print(f"- {invitado}")


nombre_mas_largo = max(invitados, key=len)
nombre_mas_corto = min(invitados, key=len)

print(f"\nInvitado con el nombre más largo: {nombre_mas_largo}")
print(f"Invitado con el nombre más corto: {nombre_mas_corto}")
