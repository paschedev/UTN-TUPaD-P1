contraseña = input("Crea tu contraseña: ")
confirmar_contraseña = input("Confirma tu contraseña: ")
if contraseña != confirmar_contraseña:
    print("Las contraseñas no coinciden.")
elif len(contraseña) < 8:
    print("La contraseña es muy corta.")
elif len(contraseña) > 14:
    print("La contraseña es muy larga.")
else:
    print("Su contraseña ha sido creada correctamente.")