def imprimirNumerosPrimos(maximo = 100):
	# prime number calculator: find all primes up to n
	primeList = []
	#for loop for checking each numbern
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
	# prime number calculator: find the first n primes

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
	max = int(input("Find primes up to what number? : "))
	count = int(input("Find how many primes?: "))
else:
	max = 100
	count = 10
	
imprimirNCantidadDeNumerosPrimos(max)
imprimirNumerosPrimos(count)