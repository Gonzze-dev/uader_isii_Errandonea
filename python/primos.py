def imprimirNumerosPrimos(maximo = 100):
	# calculadora de numeros primos: busca todos los numeros primeos hasta N
	primeList = []
	#bucle for para checkear cada numero
	for x in range(2, maximo + 1):
		isPrime = True
		index = 0
		root = int(x ** 0.5) + 1
		while index < len(primeList) and primeList[index] <= root:
			if x % primeList[index] == 0:
				isPrime = False
				break
			index += 1
		if isPrime:
			primeList.append(x)
	print(primeList)

def imprimirNCantidadDeNumerosPrimos(cantidad = 10):
	#-------------------------------------------------------------
	# calculadora de numeros primos: busca los primeros N primos

	primeList = []
	x = 2
	
	while len(primeList) < cantidad:
		isPrime = True
		index = 0
		root = int(x ** 0.5) + 1
		while index < len(primeList) and primeList[index] <= root:
			if x % primeList[index] == 0:
				isPrime = False
				break
			index += 1
		if isPrime:
			primeList.append(x)
		x += 1
	print(primeList)

opcion = input('desea ingresar datos? (y/n): ')

if opcion == 'y':
	max = int(input("buscar numeros primos hasta que numero?: "))
	count = int(input("buscar cuantos primos?: "))
else:
	max = 100
	count = 10
	
imprimirNCantidadDeNumerosPrimos(max)
imprimirNumerosPrimos(count)