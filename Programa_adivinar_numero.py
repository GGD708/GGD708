import random

intentosRealizados=0

misNombres=["Guillermo","Guille","GGD","GGD708",]

dificultades=[1,2,3]

variable1=False

dificultad1=False

dificultad2=False

dificultad3=False

dificultad_in_dificultades=False

name=input("¡Bienvenido! Por favor introduzca su nombre: ") 

if name in misNombres:
	print("¿Creador eres tú?")
	variable1=True
else:
	print("""
Hola """+name+""", yo me llamo IANA y mi creador es Guillermo.
Soy una inteligencia aritificial con la que puedes jugar,
especificamente a intentar adivinar el número que estoy pensando.""")

	dificultad=int(input("""
Este juego tiene 3 niveles de dificultad. En la dificultad 1
tendrás 8 intentos y 20 números a elegir. En la 2 solo tendrás
5 intentos, pero seguirá siendo entre los mismos números. Y en
la 3 tendrás 5 intentos, pero entre 40 números.

Escoge una dificultad: """))

	if dificultad in dificultades:
		
		dificultad_in_dificultades=True

	while dificultad_in_dificultades==False:
		dificultad=int(input("""
Esa dificultad no es valida.
Escoge una dificultad: """))
		if dificultad in dificultades:
		
			dificultad_in_dificultades=True
	
	if dificultad==1 and variable1==False and dificultad_in_dificultades==True:
			
			print("""
Has escogido la primera dificultad.""")
			
			numero=random.randint(1,20)
			
			dificultad1=True

			while intentosRealizados<8 and dificultad1==True:

				estimacion=int(input("""
Escribe un número: """))

				intentosRealizados=intentosRealizados+1

				if estimacion<1:
					print("¡Ese número es muy pequeño! Recuerda que los limites son el 1 y el 20.")
				elif estimacion<numero-2:
					print("Tu estimación es muy baja.")
				elif estimacion<numero:
					print("Tu estimación es baja")
				elif estimacion>20:
					print("!Te has pasado! Ese número es mayor de 20. Recuerda que es del 1 al 20.")
				elif estimacion>numero+2:
					print("Tu estimación es muy alta")
				elif estimacion>numero:
					print("Tu estimación es alta")
				elif estimacion==numero:
					break
		
	elif dificultad==2 and variable1==False and dificultad_in_dificultades==True:

			print("""
Has escogido la segunda dificultad.""")
			
			numero=random.randint(1,20)
			
			dificultad2=True

			while intentosRealizados<5 and dificultad2==True:

				estimacion=int(input("""
Escribe un número: """))

				intentosRealizados=intentosRealizados+1

				if estimacion<1:
					print("¡Ese número es muy pequeño! Recuerda que los limites son el 1 y el 20.")
				elif estimacion<numero-2:
					print("Tu estimación es muy baja.")
				elif estimacion<numero:
					print("Tu estimación es baja")
				elif estimacion>20:
					print("!Te has pasado! Ese número es mayor de 20. Recuerda que es del 1 al 20.")
				elif estimacion>numero+2:
					print("Tu estimación es muy alta")
				elif estimacion>numero:
					print("Tu estimación es alta")
				elif estimacion==numero:
					break

	elif dificultad==3 and variable1==False and dificultad_in_dificultades==True:
			print("""
Has escogido la tercera dificultad.""")
			
			numero=random.randint(1,40)
			
			dificultad2=True

			while intentosRealizados<5 and dificultad2==True:

				estimacion=int(input("""
Escribe un número: """))

				intentosRealizados=intentosRealizados+1

				if estimacion<1:
					print("¡Ese número es muy pequeño! Recuerda que los limites son el 1 y el 20.")
				elif estimacion<numero-2:
					print("Tu estimación es muy baja.")
				elif estimacion<numero:
					print("Tu estimación es baja")
				elif estimacion>40:
					print("!Te has pasado! Ese número es mayor de 20. Recuerda que es del 1 al 20.")
				elif estimacion>numero+2:
					print("Tu estimación es muy alta")
				elif estimacion>numero:
					print("Tu estimación es alta")
				elif estimacion==numero:
					break


if variable1==False:
	if estimacion==numero:
		intentosRealizados=str(intentosRealizados)
		print("""
¡Genial, """ + name + "! Lo has logrado en " + intentosRealizados + """ intentos.

¡Adios!""")
	else:
		numero=str(numero)
		print("Es una pena, estaba pensando en el " + numero + ". ¡Más suerte la proxima vez!")

