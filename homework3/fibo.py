def fibo(n):
    numbers = [1, 1]
    for _ in range(n-2):
        numbers.append(numbers[-2] + numbers[-1])
    return numbers[-1]

if __name__ == "__main__":
    print(fibo(6))