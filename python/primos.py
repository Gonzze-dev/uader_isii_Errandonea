def imprimirNumerosPrimos(maximo = 100):
	primeList = []
	#Imprime los numeros primos hasta el indicado por el usuario
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
	# Imprime n cantidad de numeros primos, cuantos quiera el usuario

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