# Дано целое число N. Найти все разложения числа N на простые слагаемые (например, 5 = 2 + 3, 5 = 5).
def prime_sums(number):
	if number < 2:
		return []

	primes = [candidate for candidate in range(2, number + 1)
			  if all(candidate % divisor for divisor in
					 range(2, int(candidate ** 0.5) + 1))]
	decompositions = []

	def search(remaining, first_index, summands):
		if remaining == 0:
			decompositions.append(summands.copy())
			return

		for index in range(first_index, len(primes)):
			prime = primes[index]
			if prime > remaining:
				break
			summands.append(prime)
			search(remaining - prime, index, summands)
			summands.pop()

	search(number, 0, [])
	return decompositions


array = list(map(int, input("Введите элементы массива через пробел: ").split()))
for number in array:
    decompositions = prime_sums(number)
    if decompositions:
        print(f"Разложения числа {number} на простые слагаемые:")
        for decomposition in decompositions:
            print(" + ".join(map(str, decomposition)))
    else:
        print(f"Число {number} не имеет разложений на простые слагаемые.")
        