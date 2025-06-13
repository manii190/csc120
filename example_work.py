def sets():
    n = int(input("Enter a number: "))
    numbers = list(range(1, n + 1))

    while len(numbers) > 1:
        numbers = [numbers[i] for i in range(len(numbers)) if i % 2 == 0]
        if len(numbers) % 2 != 0:
            last = numbers[-1]
            numbers = [last] + numbers

    return numbers

print(sets())
