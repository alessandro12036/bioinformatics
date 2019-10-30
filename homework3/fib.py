def rabbit_fib(n, k):
    rabbits_alive = [1, 1+k]
    for _ in range(n-2):
        offspring = k * rabbits_alive[-2]
        rabbits_alive.append(offspring + rabbits_alive[-1])

    return rabbits_alive


print(rabbit_fib(22, 1)[-2])